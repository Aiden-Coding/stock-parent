package com.aiden.stock.user.httpRsult;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ResultSearch {
    private String code;
    private List<StockBaseResp> data;
    public class StockBaseResp {
        public StockBaseResp() {
        }

        public StockBaseResp(String name, String shortName, String ticker) {
            this.name = name;
            this.shortName = shortName;
            this.ticker = ticker;
        }

        @JsonProperty("name")
        private String name;

        @JsonProperty("shortName")
        private String shortName;

        @JsonProperty("ticker")
        private String ticker;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getShortName() {
            return shortName;
        }

        public void setShortName(String shortName) {
            this.shortName = shortName;
        }

        public String getTicker() {
            return ticker;
        }

        public void setTicker(String ticker) {
            this.ticker = ticker;
        }
    }
}
