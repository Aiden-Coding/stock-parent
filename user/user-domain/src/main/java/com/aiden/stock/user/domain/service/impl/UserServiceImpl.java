package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.entity.User;
import com.aiden.stock.user.domain.dao.mapper.UserMapper;
import com.aiden.stock.user.domain.service.UserService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {

}
