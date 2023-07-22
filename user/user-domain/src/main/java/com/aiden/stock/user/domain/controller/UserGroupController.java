package com.aiden.stock.user.domain.controller;

import com.aiden.stock.comon.Result;
import com.aiden.stock.user.domain.service.UserGroupService;
import com.aiden.stock.user.dto.GroupAddReq;
import com.aiden.stock.user.dto.UserGroupResp;
import com.aiden.stock.user.dto.UserGroupStockReq;
import com.aiden.stock.user.dto.GroupStockResp;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.stereotype.Controller;

import java.util.List;

/**
 * <p>
 * 组 前端控制器
 * </p>
 *
 * @author wanggc
 * @since 2023-07-22 10:15:13
 */
@Controller
@RequestMapping("/userGroup")
public class UserGroupController {

    @Autowired
    private UserGroupService userGroupService;
    @PostMapping("/add")
    public Result addGroup(@RequestBody GroupAddReq req) {
        userGroupService.addGroup(req);
        return Result.success();
    }
    @GetMapping("/grouplist")
    public Result<List<UserGroupResp>> grouplist() {
        List<UserGroupResp> ret = userGroupService.grouplist();
        return Result.success(ret);
    }
    @PostMapping("/groupStock")
    public Result<List<GroupStockResp>> groupStock(@RequestBody UserGroupStockReq req) {
        List<GroupStockResp> ret = userGroupService.groupStock(req);
        return Result.success(ret);
    }


}
