package com.aiden.stock.user.domain.service;

import com.aiden.stock.user.domain.dao.entity.Group;
import com.aiden.stock.user.dto.GroupAddReq;
import com.aiden.stock.user.dto.GroupResp;
import com.aiden.stock.user.dto.GroupStockReq;
import com.aiden.stock.user.dto.GroupStockResp;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * <p>
 * 组 服务类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
public interface GroupService extends IService<Group> {

    void addGroup(GroupAddReq req);

    List<GroupResp> grouplist();

    List<GroupStockResp> groupStock(GroupStockReq req);
}
