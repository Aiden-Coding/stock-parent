package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.python.akapi.stock.dto.StockInfoResp;
import com.aiden.stock.user.domain.dao.mysql.entity.StockBaseInfo;
import com.aiden.stock.user.domain.dao.mysql.mapper.StockBaseInfoMapper;
import com.aiden.stock.user.domain.dto.StockInfoSearchResp;
import com.aiden.stock.user.domain.service.StockBaseInfoService;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;
import org.springframework.util.StringUtils;

import java.util.Collections;
import java.util.List;
import java.util.Objects;

/**
 * <p>
 * 股票信息 服务实现类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@Service
public class StockBaseInfoServiceImpl extends ServiceImpl<StockBaseInfoMapper, StockBaseInfo> implements StockBaseInfoService {

    @Override
    public void updateStockInfo(List<StockInfoResp> stockInfoRespList) {
        if (CollectionUtils.isEmpty(stockInfoRespList)) {
            return;
        }
        for (StockInfoResp stockInfoResp : stockInfoRespList) {
            QueryWrapper<StockBaseInfo> queryWrapper = new QueryWrapper<>();
            queryWrapper.eq("code", stockInfoResp.getCode());
            StockBaseInfo stockDB = baseMapper.selectOne(queryWrapper);
            if (Objects.nonNull(stockDB)) {
                if (!Objects.equals(stockDB.getName(),stockInfoResp.getName())) {
                    stockDB.setName(stockInfoResp.getName());
                    baseMapper.updateById(stockDB);
                }
            } else {
                stockDB = new StockBaseInfo();
                stockDB.setName(stockInfoResp.getName());
                stockDB.setCode(stockInfoResp.getCode());
                baseMapper.insert(stockDB);
            }
        }
    }

    @Override
    public List<StockInfoSearchResp> searchByKeyWord(String search) {
        if (Objects.nonNull(search) && StringUtils.hasText(search)) {
            return baseMapper.searchByKeyWord(search);
        }
        return Collections.EMPTY_LIST;
    }
}
