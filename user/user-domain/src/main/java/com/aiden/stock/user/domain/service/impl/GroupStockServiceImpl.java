package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.entity.GroupStock;
import com.aiden.stock.user.domain.dao.mapper.GroupStockMapper;
import com.aiden.stock.user.domain.service.GroupStockService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 * 组和股票关系 服务实现类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@Service
public class GroupStockServiceImpl extends ServiceImpl<GroupStockMapper, GroupStock> implements GroupStockService {

}
