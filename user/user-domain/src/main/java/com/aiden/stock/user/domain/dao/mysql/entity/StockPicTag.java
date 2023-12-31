package com.aiden.stock.user.domain.dao.mysql.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import lombok.EqualsAndHashCode;

import java.io.Serializable;
import java.util.Date;

/**
 * <p>
 * 股票标记
 * </p>
 *
 * @author xiaowa
 * @since 2023-07-22
 */
@Data
@EqualsAndHashCode(callSuper = false)
@TableName("stock_pic_tag")
public class StockPicTag implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * id
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    /**
     * 名称
     */
    private String name;

    /**
     * 代码
     */
    private String code;

    /**
     * 周期
     */
    private String timespan;

    /**
     * 标记类型
     */
    private String tagClass;

    /**
     * 标记文本
     */
    private String tagText;

    /**
     * 创建时间
     */
    private Date createDate;


}
