package com.aiden.stock.user.domain.config;


import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.ExchangeStrategies;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.support.WebClientAdapter;
import org.springframework.web.service.invoker.HttpServiceProxyFactory;

import java.time.Duration;

@Configuration
public class WebConfig {
    @Bean
    WebClient pythonClient(ObjectMapper objectMapper) {
        return WebClient.builder()
                .exchangeStrategies(ExchangeStrategies.builder()
                        .codecs(configurer -> configurer
                                .defaultCodecs()
                                .maxInMemorySize(10 * 1024 * 1024))
                        .build())
                .baseUrl("http://localhost:8080/pythonAkApi")
                .build();
    }

    @SneakyThrows
    @Bean
    com.aiden.stock.python.akapi.stock.StockApi akStockApi(WebClient pythonClient) {
        HttpServiceProxyFactory httpServiceProxyFactory =
                HttpServiceProxyFactory.builder(WebClientAdapter.forClient(pythonClient)).blockTimeout(Duration.ofMinutes(5))
                        .build();
        return httpServiceProxyFactory.createClient(com.aiden.stock.python.akapi.stock.StockApi.class);
    }
}