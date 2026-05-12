-- 订单表
CREATE TABLE `orders` (
    `id` INT NOT NULL AUTO_INCREMENT COMMENT '订单ID',
    `user_id` INT NOT NULL COMMENT '用户ID，关联users.id',
    `amount` DECIMAL(10,2) NOT NULL COMMENT '订单金额（单位：元）',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (`id`),
    KEY `idx_user_id` (`user_id`),
    CONSTRAINT `fk_orders_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='订单表';

select * from orders;



-- =============================================
-- 2. 插入订单数据（每个用户有 1~3 条订单）
-- =============================================
INSERT INTO `orders` (`user_id`, `amount`, `create_time`) VALUES
-- 用户张三 (id=1) 的订单
(1, 99.50, '2025-03-01 10:23:00'),
(1, 245.00, '2025-03-10 15:10:22'),
(1, 88.00, '2025-04-01 09:45:33'),

-- 用户李四 (id=2) 的订单
(2, 1280.00, '2025-03-05 14:20:00'),
(2, 550.00, '2025-03-18 11:08:17'),

-- 用户王芳 (id=3) 的订单
(3, 3999.99, '2025-02-28 20:30:00'),
(3, 199.90, '2025-03-25 08:12:44'),
(3, 56.80, '2025-04-03 18:22:01'),

-- 用户赵磊 (id=4) 的订单
(4, 888.88, '2025-03-12 13:45:00'),

-- 用户孙丽 (id=5) 的订单
(5, 45.00, '2025-03-20 09:00:00'),
(5, 367.50, '2025-03-28 16:37:19'),
(5, 1299.00, '2025-04-02 12:10:50'),

-- 用户周涛 (id=6) 的订单
(6, 229.90, '2025-03-30 10:05:00'),
(6, 612.30, '2025-04-05 14:22:33');