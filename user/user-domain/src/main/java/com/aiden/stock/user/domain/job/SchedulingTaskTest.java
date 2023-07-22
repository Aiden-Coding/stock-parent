package com.aiden.stock.user.domain.job;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class SchedulingTaskTest {

    /**
     * 每五秒执行一次
     */
    @Scheduled(cron = "*/5 * * * * ?")
    private void printNowDate() {
        long nowDateTime = System.currentTimeMillis();
        System.out.println("固定定时任务执行:--->"+nowDateTime+"，此任务为每五秒执行一次");
    }

}
