package com.aiden.stock.user.domain.dao.mysql.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import lombok.Getter;
import lombok.Setter;

/**
 * <p>
 * 组
 * </p>
 *
 * @author wanggc
 * @since 2023-07-22 10:15:13
 */
@Getter
@Setter
@TableName("user_group")
public class UserGroup implements Serializable {

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
}
