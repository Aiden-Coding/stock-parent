package com.aiden.stock.user.domain.controller;

import com.aiden.stock.comon.Result;
import com.aiden.stock.comon.util.SnowflakeIdGenerator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/common")
public class CommonController {
    @Autowired
    private SnowflakeIdGenerator snowflakeIdGenerator;
    @GetMapping("/generateId")
    public Result<Long> generateId() {
        return Result.success(snowflakeIdGenerator.generateId());
    }
}
