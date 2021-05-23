-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.23 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for company
DROP DATABASE IF EXISTS `company`;
CREATE DATABASE IF NOT EXISTS `company` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `company`;

-- Dumping structure for table company.customer
DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phone` varchar(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table company.customer: ~0 rows (approximately)
DELETE FROM `customer`;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` (`id`, `name`, `phone`) VALUES
	(1, 'Ahmed Shaban', '0124578944'),
	(2, 'Ali Mohamed', '0124578954'),
	(3, 'Salma Ali', '0124578963'),
	(4, 'Mosa Zaki', '0145789654'),
	(5, 'Hana Sheba', '01345678987');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

-- Dumping structure for table company.order
DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `customer` int NOT NULL,
  `product` int NOT NULL,
  `Quantity` int NOT NULL DEFAULT '1',
  `address` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `state` set('Preparing','Shipping','Delivered') NOT NULL DEFAULT 'Preparing',
  PRIMARY KEY (`customer`,`product`),
  KEY `product` (`product`),
  CONSTRAINT `customer` FOREIGN KEY (`customer`) REFERENCES `customer` (`id`),
  CONSTRAINT `product` FOREIGN KEY (`product`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table company.order: ~0 rows (approximately)
DELETE FROM `order`;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` (`customer`, `product`, `Quantity`, `address`, `date`, `state`) VALUES
	(1, 2, 1, 'Giza', '2021-04-14', 'Preparing'),
	(1, 12, 2, 'Giza', '2021-04-14', 'Preparing'),
	(2, 13, 10, 'Cairo', '2021-04-07', 'Shipping'),
	(3, 4, 2, 'Zagazig', '2020-01-11', 'Delivered'),
	(4, 6, 7, 'Sharqia', '2021-03-15', 'Delivered'),
	(4, 7, 7, 'Sharqia', '2021-03-15', 'Delivered'),
	(4, 9, 11, 'Sharqia', '2021-04-01', 'Delivered'),
	(5, 13, 1, 'Cairo', '2021-04-12', 'Shipping');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;

-- Dumping structure for table company.product
DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` float NOT NULL DEFAULT '0',
  `supplier` int NOT NULL,
  `supply date` date NOT NULL,
  `state` set('In store','Sold out') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `supplier` (`supplier`),
  CONSTRAINT `supplier` FOREIGN KEY (`supplier`) REFERENCES `supplier` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table company.product: ~0 rows (approximately)
DELETE FROM `product`;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` (`id`, `name`, `price`, `supplier`, `supply date`, `state`) VALUES
	(1, 'Mi 11', 4000, 2, '2021-04-14', 'In store'),
	(2, 'Mi 10 pro', 5999, 2, '2021-04-14', 'In store'),
	(3, 'Note 5', 3000, 2, '2017-03-08', 'Sold out'),
	(4, 'y7', 3000, 3, '2018-04-14', 'Sold out'),
	(5, 'Nova', 6000, 3, '2020-04-14', 'In store'),
	(6, 'N11', 4555, 1, '2018-12-15', 'Sold out'),
	(7, 'N12', 4000, 1, '2020-01-10', 'In store'),
	(8, 'N13', 3999, 1, '2021-04-14', 'In store'),
	(9, 'Zeko22', 2500, 5, '2020-12-14', 'In store'),
	(10, 'Zeko+', 3100, 5, '2021-01-12', 'In store'),
	(11, 'Zeko Pro', 3666, 5, '2021-04-14', 'In store'),
	(12, 'One V11', 5999, 4, '2020-08-14', 'In store'),
	(13, 'One Max', 6999, 4, '2020-11-08', 'In store');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- Dumping structure for table company.supplier
DROP TABLE IF EXISTS `supplier`;
CREATE TABLE IF NOT EXISTS `supplier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table company.supplier: ~0 rows (approximately)
DELETE FROM `supplier`;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` (`id`, `name`, `address`, `phone`) VALUES
	(1, 'Nokia', 'USA', '+1457855447'),
	(2, 'Xiaomi', 'China', '+781125447'),
	(3, 'Huawie', 'China', '+124578963'),
	(4, 'One+', 'France', '+1247856'),
	(5, 'Pyrimeds', 'Egypt', '01245678951');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
