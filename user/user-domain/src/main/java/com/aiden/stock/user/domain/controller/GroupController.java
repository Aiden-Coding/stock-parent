package com.aiden.stock.user.domain.controller;


import com.aiden.stock.comon.Result;
import com.aiden.stock.user.domain.service.GroupService;
import com.aiden.stock.user.dto.GroupAddReq;
import com.aiden.stock.user.dto.GroupResp;
import com.aiden.stock.user.dto.GroupStockReq;
import com.aiden.stock.user.dto.GroupStockResp;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * <p>
 * 组 前端控制器
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@RestController
@RequestMapping("/group")
public class GroupController {

    @Autowired
    private GroupService groupService;
    @PostMapping("/add")
    public Result addGroup(@RequestBody GroupAddReq req) {
        groupService.addGroup(req);
        return Result.success();
    }
    @GetMapping("/grouplist")
    public Result<List<GroupResp>> grouplist() {
        List<GroupResp> ret = groupService.grouplist();
        return Result.success(ret);
    }
    @PostMapping("/groupStock")
    public Result<List<GroupStockResp>> groupStock(@RequestBody GroupStockReq req) {
        List<GroupStockResp> ret = groupService.groupStock(req);
        return Result.success(ret);
    }

}

