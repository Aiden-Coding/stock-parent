package com.aiden.stock.user.domain.service;

import com.aiden.stock.user.domain.dao.mysql.entity.StockPicTag;
import com.aiden.stock.user.dto.StockPicTagAddReq;
import com.aiden.stock.user.dto.StockPicTagResp;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * <p>
 * 股票标记 服务类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
public interface StockPicTagService extends IService<StockPicTag> {

    void add(StockPicTagAddReq req);

    void deleteById(Long id);

    List<StockPicTagResp> getPicTagByCode(String code,String timespan);
}
