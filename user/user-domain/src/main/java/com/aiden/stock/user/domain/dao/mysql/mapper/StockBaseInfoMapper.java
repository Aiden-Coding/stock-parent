package com.aiden.stock.user.domain.dao.mysql.mapper;

import com.aiden.stock.user.domain.dao.mysql.entity.StockBaseInfo;
import com.aiden.stock.user.domain.dto.StockInfoSearchResp;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * <p>
 * 股票信息 Mapper 接口
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
public interface StockBaseInfoMapper extends BaseMapper<StockBaseInfo> {
    List<StockInfoSearchResp> searchByKeyWord(@Param("search") String search);
}
