package com.aiden.stock.user.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
public class StockBaseResp {

    @JsonProperty("name")
    private String name;

    @JsonProperty("shortName")
    private String shortName;

    @JsonProperty("ticker")
    private String ticker;
}
