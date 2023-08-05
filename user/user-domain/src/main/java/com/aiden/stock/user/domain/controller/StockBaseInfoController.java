package com.aiden.stock.user.domain.controller;


import com.aiden.stock.comon.Result;
import com.aiden.stock.python.akapi.stock.StockApi;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * <p>
 * 股票信息 前端控制器
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@RestController
@RequestMapping("/stockBaseInfo")
public class StockBaseInfoController {

    @Autowired
    private StockApi stockApi;
    @GetMapping("/search")
    public Result search() {
        Result result = stockApi.stock_info_a_code_name();
       return result;
    }
}

