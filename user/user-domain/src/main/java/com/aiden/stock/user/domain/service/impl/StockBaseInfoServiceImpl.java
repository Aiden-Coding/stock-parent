package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.entity.StockBaseInfo;
import com.aiden.stock.user.domain.dao.mapper.StockBaseInfoMapper;
import com.aiden.stock.user.domain.service.StockBaseInfoService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

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

}
