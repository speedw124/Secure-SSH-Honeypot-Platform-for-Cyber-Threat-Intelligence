-- MySQL dump 10.13  Distrib 8.0.32
-- Host: localhost    Database: corporate_users
-- ------------------------------------------------------

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) UNIQUE,
  `password_hash` varchar(255) DEFAULT NULL,
  `role` varchar(20) DEFAULT 'employee',
  PRIMARY KEY (`id`)
);

INSERT INTO `users` VALUES 
(1,'Admin User','admin@company-prod.com','$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi','superuser'),
(2,'Finance Manager','finance@company-prod.com','$2y$10$e0MYzX'manager'),
(3,'IT Support','support@company-prod.com','$2y$10$7vR9','staff');

-- Dump completed on 2026-03-10 04:00:01

