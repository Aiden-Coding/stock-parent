package com.aiden.stock.python.akapi.stock;

import com.aiden.stock.comon.Result;
import com.aiden.stock.python.akapi.stock.dto.StockInfoResp;
import org.springframework.web.service.annotation.GetExchange;
import org.springframework.web.service.annotation.HttpExchange;

import java.util.List;

@HttpExchange(url = "/stock", accept = "application/json", contentType = "application/json")
public interface StockApi {
    @GetExchange("/stock_info_a_code_name")
    Result<List<StockInfoResp>> stock_info_a_code_name();
}
