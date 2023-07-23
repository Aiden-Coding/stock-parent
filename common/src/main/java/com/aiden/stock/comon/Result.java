package com.aiden.stock.comon;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@JsonIgnoreProperties(ignoreUnknown = true)
@AllArgsConstructor
@NoArgsConstructor
public class Result<T> {
    private String code;
    private T data;

    public static <T> Result<T> success() {
        return new Result("0000", "success");
    }
    public static <T> Result<T> success(T data) {
        return new Result("0000", data);
    }
}
