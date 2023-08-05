package com.aiden.stock.user.domain.controller;


import com.aiden.stock.comon.Result;
import com.aiden.stock.user.domain.service.StockPicTagService;
import com.aiden.stock.user.dto.StockPicTagAddReq;
import com.aiden.stock.user.dto.StockPicTagResp;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * <p>
 * 股票标记 前端控制器
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@RestController
@RequestMapping("/stockPicTag")
public class StockPicTagController {

    @Autowired
    private StockPicTagService stockPicTagService;
    @PostMapping("/add")
    public Result add(@RequestBody StockPicTagAddReq req) {
        stockPicTagService.add(req);
        return Result.success();
    }

    @PostMapping("/delete/{id}")
    public Result deleteById(@PathVariable Long id) {
        stockPicTagService.deleteById(id);
        return Result.success();
    }

    @PostMapping("/getPicTag")
    public Result<List<StockPicTagResp>> getPicTagByCode(@RequestParam("code") String code,@RequestParam("timespan") String timespan) {
        List<StockPicTagResp> ret = stockPicTagService.getPicTagByCode(code,timespan);
        return Result.success(ret);
    }

}

