package com.aiden.stock.user.domain.job;

import com.aiden.stock.comon.Result;
import com.aiden.stock.python.akapi.stock.StockApi;
import com.aiden.stock.python.akapi.stock.dto.StockInfoResp;
import com.aiden.stock.user.domain.service.StockBaseInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class SchedulingTaskTest {
    @Autowired
    private StockApi stockApi;
    @Autowired
    private StockBaseInfoService stockBaseInfoService;
    /**
     * 该任务将会在每天工作日的 9 点 25 分执行。
     */
    @Scheduled(cron = "0 25 9 * * MON-FRI")
    private void updateStockInfo() {
        Result<List<StockInfoResp>> result = stockApi.stock_info_a_code_name();
        stockBaseInfoService.updateStockInfo(result.getData());
    }
}
