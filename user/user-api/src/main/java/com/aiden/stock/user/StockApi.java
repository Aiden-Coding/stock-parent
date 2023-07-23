package com.aiden.stock.user;

import com.aiden.stock.user.httpRsult.ResultSearch;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.service.annotation.GetExchange;
import org.springframework.web.service.annotation.HttpExchange;


@HttpExchange("/stock")
public interface StockApi {
    @GetExchange("/search")
    ResultSearch search(@RequestParam("search") String search);
}
