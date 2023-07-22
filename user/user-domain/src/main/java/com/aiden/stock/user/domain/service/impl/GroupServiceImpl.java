package com.aiden.stock.user.domain.service.impl;

import com.aiden.stock.user.domain.dao.entity.Group;
import com.aiden.stock.user.domain.dao.mapper.GroupMapper;
import com.aiden.stock.user.domain.service.GroupService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 * 组 服务实现类
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@Service
public class GroupServiceImpl extends ServiceImpl<GroupMapper, Group> implements GroupService {

}
