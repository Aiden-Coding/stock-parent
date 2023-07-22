package com.aiden.stock.user.dto;

import lombok.Data;

import java.util.List;

@Data
public class UserLoginResp {
    private String username;
    private String password;
    private String role;
    private Integer roleId;
    private List<String> permissions;
}
