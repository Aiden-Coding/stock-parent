package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.entity.Group;
import com.aiden.stock.user.domain.dao.mapper.GroupMapper;
import com.aiden.stock.user.domain.service.GroupService;
import com.aiden.stock.user.dto.GroupAddReq;
import com.aiden.stock.user.dto.GroupResp;
import com.aiden.stock.user.dto.GroupStockReq;
import com.aiden.stock.user.dto.GroupStockResp;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;

import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * 组 服务实现类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@Service
public class GroupServiceImpl extends ServiceImpl<GroupMapper, Group> implements GroupService {

    @Override
    public void addGroup(GroupAddReq req) {
        Group group = new Group();
        group.setName(req.getName());
        baseMapper.insert(group);
    }

    @Override
    public List<GroupResp> grouplist() {
        List<GroupResp> ret = new ArrayList<>();
        QueryWrapper queryWrapper = new QueryWrapper<>();
        queryWrapper.isNotNull("id");
        List<Group> retDB = baseMapper.selectList(queryWrapper);
        if (!CollectionUtils.isEmpty(retDB)) {
            retDB.forEach( x -> {
                GroupResp retTmp = new GroupResp();
                BeanUtils.copyProperties(x,retTmp);
                ret.add(retTmp);
            });
        }
        return ret;
    }

    @Override
    public List<GroupStockResp> groupStock(GroupStockReq req) {
        return null;
    }
}
