package com.aiden.stock.user.domain.dao.mapper;

import com.aiden.stock.user.domain.dao.entity.Group;
import com.aiden.stock.user.dto.GroupStockResp;
import com.baomidou.dynamic.datasource.annotation.DS;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * <p>
 * 组 Mapper 接口
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@DS("master")
public interface GroupMapper extends BaseMapper<Group> {
    List<GroupStockResp> queryGroupStock(@Param("groupId") Long groupId,@Param("groupName") String groupName);

}
