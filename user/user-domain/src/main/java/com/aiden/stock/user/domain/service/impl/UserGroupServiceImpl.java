package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.mysql.entity.UserGroup;
import com.aiden.stock.user.domain.dao.mysql.mapper.UserGroupMapper;
import com.aiden.stock.user.domain.service.UserGroupService;
import com.aiden.stock.user.dto.GroupAddReq;
import com.aiden.stock.user.dto.UserGroupResp;
import com.aiden.stock.user.dto.UserGroupStockReq;
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
 * @author wanggc
 * @since 2023-07-22 10:15:13
 */
@Service
public class UserGroupServiceImpl extends ServiceImpl<UserGroupMapper, UserGroup> implements UserGroupService {

    @Override
    public void addGroup(GroupAddReq req) {
        UserGroup group = new UserGroup();
        group.setName(req.getName());
        baseMapper.insert(group);
    }

    @Override
    public List<UserGroupResp> grouplist() {
        List<UserGroupResp> ret = new ArrayList<>();
        QueryWrapper queryWrapper = new QueryWrapper<>();
        queryWrapper.isNotNull("id");
        List<UserGroup> retDB = baseMapper.selectList(queryWrapper);
        if (!CollectionUtils.isEmpty(retDB)) {
            retDB.forEach( x -> {
                UserGroupResp retTmp = new UserGroupResp();
                BeanUtils.copyProperties(x,retTmp);
                ret.add(retTmp);
            });
        }
        return ret;
    }

    @Override
    public List<GroupStockResp> groupStock(UserGroupStockReq req) {
        return baseMapper.queryGroupStock(null,req.getGroupName());
    }
}
