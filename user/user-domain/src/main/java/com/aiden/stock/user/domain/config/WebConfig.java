package com.aiden.stock.user.domain.config;


import com.aiden.stock.user.StockApi;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.support.WebClientAdapter;
import org.springframework.web.service.invoker.HttpServiceProxyFactory;

@Configuration
public class WebConfig {
    @Bean
    WebClient webClient(ObjectMapper objectMapper) {
        return WebClient.builder()
                .baseUrl("http://localhost:1338/")
                .build();
    }
    @SneakyThrows
    @Bean
    StockApi stockApi(WebClient webClient) {
        HttpServiceProxyFactory httpServiceProxyFactory =
                HttpServiceProxyFactory.builder(WebClientAdapter.forClient(webClient))
                        .build();
        return httpServiceProxyFactory.createClient(StockApi.class);
    }
}