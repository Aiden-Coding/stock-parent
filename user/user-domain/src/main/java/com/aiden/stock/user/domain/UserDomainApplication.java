package com.aiden.stock.user.domain;

import org.mybatis.spring.annotation.MapperScan;
import org.mybatis.spring.annotation.MapperScans;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@MapperScan(basePackages = "com.aiden.stock.user.domain.dao.mapper")
public class UserDomainApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserDomainApplication.class,args);
    }
}
