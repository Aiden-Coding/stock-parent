package com.aiden.stock.user.domain;

import com.aiden.stock.comon.util.SnowflakeIdGenerator;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.scheduling.annotation.EnableScheduling;

@EnableScheduling
@SpringBootApplication
@MapperScan(basePackages = "com.aiden.stock.user.domain.dao")
public class UserDomainApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserDomainApplication.class,args);
    }

    @Bean
    public SnowflakeIdGenerator snowflakeIdGenerator() {
        return new SnowflakeIdGenerator(1);
    }
}
