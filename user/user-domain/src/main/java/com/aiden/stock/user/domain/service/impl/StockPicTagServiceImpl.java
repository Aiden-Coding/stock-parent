package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.mysql.entity.StockPicTag;
import com.aiden.stock.user.domain.dao.mysql.mapper.StockPicTagMapper;
import com.aiden.stock.user.domain.service.StockPicTagService;
import com.aiden.stock.user.dto.StockPicTagAddReq;
import com.aiden.stock.user.dto.StockPicTagResp;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * <p>
 * 股票标记 服务实现类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@Service
public class StockPicTagServiceImpl extends ServiceImpl<StockPicTagMapper, StockPicTag> implements StockPicTagService {

    @Override
    public void add(StockPicTagAddReq req) {
        StockPicTag stockPicTag = new StockPicTag();
        BeanUtils.copyProperties(req,stockPicTag);
        stockPicTag.setCreateDate(new Date());
        baseMapper.insert(stockPicTag);
    }

    @Override
    public void deleteById(Long id) {
        baseMapper.deleteById(id);
    }

    @Override
    public List<StockPicTagResp> getPicTagByCode(String code,String timespan) {
        QueryWrapper<StockPicTag> query = new QueryWrapper<>();
        query.eq("code",code);
        query.eq("timespan",timespan);
        List<StockPicTagResp> ret = new ArrayList<>();
        List<StockPicTag> retDB = baseMapper.selectList(query);
        if (!CollectionUtils.isEmpty(retDB)) {
            retDB.forEach(x -> {
                StockPicTagResp retT = new StockPicTagResp();
                BeanUtils.copyProperties(x,retT);
                ret.add(retT);
            });
        }
        return ret;
    }
}
