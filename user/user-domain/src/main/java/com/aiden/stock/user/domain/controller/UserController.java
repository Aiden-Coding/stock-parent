package com.aiden.stock.user.domain.controller;


import com.aiden.stock.comon.Result;
import com.aiden.stock.user.dto.UserLoginResp;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@RestController
@RequestMapping("/user")
public class UserController {

    @PostMapping("/login")
    public Result login() {
        UserLoginResp ret = new UserLoginResp();
        ret.setUsername("admin");
        ret.setPassword("admin");
        ret.setRole("admin");
        ret.setRoleId(1);
        List<String> permissions = new ArrayList<>();
        ret.setPermissions(permissions);
        permissions.add("*.*.*");
        return Result.success(ret);
    }
    @GetMapping("/loginOut")
    public Result logout(){
        return Result.success("成功");
    }
}

