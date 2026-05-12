-- 用户表
CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    `name` VARCHAR(50) NOT NULL COMMENT '用户姓名',
    `city` VARCHAR(50) NOT NULL COMMENT '所在城市',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户表';

select * from users


-- =============================================
-- 1. 插入用户数据（先插入 users，确保外键引用存在）
-- =============================================
INSERT INTO `users` (`name`, `city`) VALUES
('张三', '北京'),
('李四', '上海'),
('王芳', '广州'),
('赵磊', '深圳'),
('孙丽', '成都'),
('周涛', '杭州');
