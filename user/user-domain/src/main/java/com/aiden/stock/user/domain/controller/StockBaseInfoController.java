package com.aiden.stock.user.domain.controller;


import com.aiden.stock.comon.Result;
import com.aiden.stock.user.domain.dto.StockInfoSearchResp;
import com.aiden.stock.user.domain.service.StockBaseInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

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
    private StockBaseInfoService stockBaseInfoService;
    @GetMapping("/search")
    public Result<List<StockInfoSearchResp>> search(@RequestParam("search") String search) {
        List<StockInfoSearchResp> ret = stockBaseInfoService.searchByKeyWord(search);
       return Result.success(ret);
    }
}

