package com.aiden.stock.user.domain.service;

import com.aiden.stock.user.domain.dao.mysql.entity.UserGroup;
import com.aiden.stock.user.dto.GroupAddReq;
import com.aiden.stock.user.dto.UserGroupResp;
import com.aiden.stock.user.dto.UserGroupStockReq;
import com.aiden.stock.user.dto.GroupStockResp;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * <p>
 * 组 服务类
 * </p>
 *
 * @author wanggc
 * @since 2023-07-22 10:15:13
 */
public interface UserGroupService extends IService<UserGroup> {

    void addGroup(GroupAddReq req);

    List<UserGroupResp> grouplist();

    List<GroupStockResp> groupStock(UserGroupStockReq req);
}
