package com.aiden.stock.user.domain.dao.mapper;

import com.aiden.stock.user.domain.dao.entity.UserGroup;
import com.aiden.stock.user.dto.GroupStockResp;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * <p>
 * 组 Mapper 接口
 * </p>
 *
 * @author wanggc
 * @since 2023-07-22 10:15:13
 */
public interface UserGroupMapper extends BaseMapper<UserGroup> {

    List<GroupStockResp> queryGroupStock(@Param("groupId") Long groupId, @Param("groupName") String groupName);
}
