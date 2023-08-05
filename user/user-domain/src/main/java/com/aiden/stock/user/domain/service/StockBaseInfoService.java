package com.aiden.stock.user.domain.service;

import com.aiden.stock.python.akapi.stock.dto.StockInfoResp;
import com.aiden.stock.user.domain.dao.mysql.entity.StockBaseInfo;
import com.aiden.stock.user.domain.dto.StockInfoSearchResp;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * <p>
 * 股票信息 服务类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
public interface StockBaseInfoService extends IService<StockBaseInfo> {
    void updateStockInfo(List<StockInfoResp> stockInfoRespList);

    List<StockInfoSearchResp> searchByKeyWord(String search);
}
