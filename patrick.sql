-- Create the database
CREATE DATABASE my_company;

-- Switch to that database
use my_company;

-- Create the clients table
Create Table: CREATE TABLE `clients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(55) NOT NULL,
  `lastname` varchar(55) NOT NULL,
  `age` tinyint NOT NULL,
  `notes` longtext,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `country` varchar(100) NOT NULL DEFAULT 'USA',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Populate clients table
INSERT INTO `clients` VALUES (1,'Nancy','Smith',32,'Some notes for Nancy','1234 Colingwood, California','nancy.smith@gmail.com','USA'),(2,'Brian','Collins',45,'Some notes for Brian','432 Somerset West, Illinois','brian.collins@gmail.com','USA'),(3,'Jonny','Okito',57,'This is our new CEO','1460 Major Oaks, Pickeriing, Ontario','jokito3000@gmail.com','Canada'),(4,'Nancy','Kensington',35,'This is some chick from Atlanta','12345 Common Street, Atlanta','n.kensington@gmail.com','USA'),(5,'Meghan','Nelson',35,'This is our new secretary','Some random address, Vancouver','m.nelson@gmail.com','Canada');
