package com.aiden.stock.user;

import com.aiden.stock.comon.Result;
import com.aiden.stock.user.dto.StockBaseResp;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.service.annotation.GetExchange;
import org.springframework.web.service.annotation.HttpExchange;

import java.util.List;


@HttpExchange(url = "/stock", accept = "application/json", contentType = "application/json")
public interface StockApi {
    @GetExchange("/search")
    Result<List<StockBaseResp>> search(@RequestParam("search") String search);
}
