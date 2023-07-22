package com.aiden.stock.comon;

import lombok.Data;

@Data
public class Result<T> {
    private String code;
    private T data;

    public Result(String code, T data) {
        this.code = code;
        this.data = data;
    }
    public static <T> Result<T> success() {
        return new Result("0000", "success");
    }
    public static <T> Result<T> success(T data) {
        return new Result("0000", data);
    }
}
