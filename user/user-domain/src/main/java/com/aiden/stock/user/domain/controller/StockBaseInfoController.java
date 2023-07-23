package com.aiden.stock.user.domain.controller;


import com.aiden.stock.comon.Result;
import com.aiden.stock.user.StockApi;
import com.aiden.stock.user.dto.StockBaseResp;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * <p>
 * 股票信息 前端控制器
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@RestController
@RequestMapping("/stockBaseInfo")
public class StockBaseInfoController {

    @Autowired
    private StockApi stockApi;
    @GetMapping("/search")
    public Result search(@RequestParam("search") String search) {
//        String retstr = stockApi.search(search);
//        System.out.println(retstr);
//        retstr = retstr.substring(1,retstr.length()-1);
//        JSONObject obj= JSONObject.parseObject(retstr);
//        JSONArray arr=obj.getJSONArray("data");
//        StockBaseResp[] collection =arr.toJavaObject(StockBaseResp[].class);
//        String js=JSONObject.toJSONString(arr, SerializerFeature.WriteClassName);//将array数组转换成字符串
//        List<StockBaseResp>  collection = JSONObject.parseArray(js, StockBaseResp.class);
//
//        TypeReference<Result<List<StockBaseResp>>> typeRef = new TypeReference<Result<List<StockBaseResp>>>() {};
//        Result<List<StockBaseResp>> result = JSON.parseObject(retstr, typeRef);
        Result result = stockApi.search(search);
       return result;
//       return Result.success(collection);
    }

    public static void main(String[] args) {
        String str = "{\"data\": [{\"name\": \"\\u7f8e\\u5229\\u4e91\", \"shortName\": \"\\u7f8e\\u5229\\u4e91\", \"ticker\": \"000815\"}], \"code\": \"0000\"}";
        JSONObject obj=JSONObject.parseObject(str);
        JSONArray arr=obj.getJSONArray("data");
        StockBaseResp[] collection =arr.toJavaObject(StockBaseResp[].class);

    }
}

