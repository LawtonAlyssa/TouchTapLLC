-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema shop
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema shop
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shop` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `shop` ;

-- -----------------------------------------------------
-- Table `shop`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(50) NOT NULL,
  `middleName` VARCHAR(50) NULL DEFAULT NULL,
  `lastName` VARCHAR(50) NOT NULL,
  `mobile` VARCHAR(15) NULL DEFAULT NULL,
  `email` VARCHAR(50) NOT NULL,
  `passwordHash` VARCHAR(32) NOT NULL,
  `admin` TINYINT(1) UNSIGNED ZEROFILL NOT NULL DEFAULT '0',
  `registeredAt` DATETIME NOT NULL,
  `lastLogin` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `mobile_UNIQUE` (`mobile` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 109
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `shop`.`cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`cart` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `userId` INT NULL DEFAULT NULL,
  `sessionId` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `token` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `status` SMALLINT NOT NULL DEFAULT '0',
  `firstName` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `middleName` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `lastName` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `mobile` VARCHAR(15) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `email` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `line1` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `line2` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `city` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `province` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `country` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `createdAt` DATETIME NOT NULL,
  `updatedAt` DATETIME NULL DEFAULT NULL,
  `content` TEXT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_cart_user` (`userId` ASC) VISIBLE,
  CONSTRAINT `fk_cart_user`
    FOREIGN KEY (`userId`)
    REFERENCES `shop`.`user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `shop`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(75) NOT NULL,
  `metaTitle` VARCHAR(100) NOT NULL,
  `slug` VARCHAR(100) NOT NULL,
  `summary` TEXT NULL DEFAULT NULL,
  `type` SMALLINT NOT NULL DEFAULT '0',
  `price` FLOAT NOT NULL DEFAULT '0',
  `createdAt` DATETIME NOT NULL,
  `content` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `slug_UNIQUE` (`slug` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `shop`.`cart_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`cart_item` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `productId` INT NOT NULL,
  `cartId` BIGINT NOT NULL,
  `sku` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `price` FLOAT NOT NULL DEFAULT '0',
  `discount` FLOAT NOT NULL DEFAULT '0',
  `quantity` SMALLINT NOT NULL DEFAULT '0',
  `active` TINYINT(1) NOT NULL DEFAULT '0',
  `createdAt` DATETIME NOT NULL,
  `updatedAt` DATETIME NULL DEFAULT NULL,
  `content` TEXT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_cart_item_product` (`productId` ASC) VISIBLE,
  CONSTRAINT `fk_cart_item_product`
    FOREIGN KEY (`productId`)
    REFERENCES `shop`.`product` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `shop`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`order` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `userId` INT NULL DEFAULT NULL,
  `sessionId` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `token` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `status` SMALLINT NOT NULL DEFAULT '0',
  `subTotal` FLOAT NOT NULL DEFAULT '0',
  `tax` FLOAT NOT NULL DEFAULT '0',
  `shipping` FLOAT NOT NULL DEFAULT '0',
  `total` FLOAT NOT NULL DEFAULT '0',
  `grandTotal` FLOAT NOT NULL DEFAULT '0',
  `firstName` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `middleName` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `lastName` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `mobile` VARCHAR(15) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `email` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `line1` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `line2` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `city` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `province` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `country` VARCHAR(50) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `createdAt` DATETIME NOT NULL,
  `updatedAt` DATETIME NULL DEFAULT NULL,
  `content` TEXT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_order_user` (`userId` ASC) VISIBLE,
  CONSTRAINT `fk_order_user`
    FOREIGN KEY (`userId`)
    REFERENCES `shop`.`user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `shop`.`order_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`order_item` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `productId` INT NOT NULL,
  `orderId` BIGINT NOT NULL,
  `sku` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `price` FLOAT NOT NULL DEFAULT '0',
  `quantity` SMALLINT NOT NULL DEFAULT '0',
  `createdAt` DATETIME NOT NULL,
  `updatedAt` DATETIME NULL DEFAULT NULL,
  `content` TEXT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_order_item_product` (`productId` ASC) VISIBLE,
  CONSTRAINT `fk_order_item_product`
    FOREIGN KEY (`productId`)
    REFERENCES `shop`.`product` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `shop`.`scheduled`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`scheduled` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `slug` VARCHAR(45) NOT NULL,
  `startTime` VARCHAR(45) NULL DEFAULT NULL,
  `endTime` VARCHAR(45) NULL DEFAULT NULL,
  `availability` SMALLINT NOT NULL,
  `userId` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `slug_idx` (`slug` ASC) VISIBLE,
  INDEX `userId_idx` (`userId` ASC) VISIBLE,
  CONSTRAINT `slug`
    FOREIGN KEY (`slug`)
    REFERENCES `shop`.`product` (`slug`),
  CONSTRAINT `userId`
    FOREIGN KEY (`userId`)
    REFERENCES `shop`.`user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `shop`.`transaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shop`.`transaction` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `userId` INT NOT NULL,
  `orderId` BIGINT NOT NULL,
  `code` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `type` SMALLINT NOT NULL DEFAULT '0',
  `mode` SMALLINT NOT NULL DEFAULT '0',
  `status` SMALLINT NOT NULL DEFAULT '0',
  `createdAt` DATETIME NOT NULL,
  `updatedAt` DATETIME NULL DEFAULT NULL,
  `content` TEXT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_transaction_user` (`userId` ASC) VISIBLE,
  CONSTRAINT `fk_transaction_user`
    FOREIGN KEY (`userId`)
    REFERENCES `shop`.`user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
