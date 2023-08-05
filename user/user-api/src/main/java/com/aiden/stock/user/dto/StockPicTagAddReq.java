package com.aiden.stock.user.dto;

import lombok.Data;

import java.util.Date;

@Data
public class StockPicTagAddReq {
    private Long id;
    private String name;
    private String code;
    private String timespan;
    private String tagClass;
    private String tagText;
    private Date createDate;
}
