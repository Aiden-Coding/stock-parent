package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.entity.UserGroupStock;
import com.aiden.stock.user.domain.dao.mapper.UserGroupStockMapper;
import com.aiden.stock.user.domain.service.UserGroupStockService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 * 组和股票关系 服务实现类
 * </p>
 *
 * @author wanggc
 * @since 2023-07-22 10:22:59
 */
@Service
public class UserGroupStockServiceImpl extends ServiceImpl<UserGroupStockMapper, UserGroupStock> implements UserGroupStockService {

}
