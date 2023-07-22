package com.aiden.stock.user.domain.dao.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import lombok.Getter;
import lombok.Setter;

/**
 * <p>
 * 组和股票关系
 * </p>
 *
 * @author wanggc
 * @since 2023-07-22 10:22:59
 */
@Getter
@Setter
@TableName("user_group_stock")
public class UserGroupStock implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * id
     */
      @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    /**
     * 组名称
     */
    private Long groupId;

    /**
     * 股票code
     */
    private String stockCode;
}
