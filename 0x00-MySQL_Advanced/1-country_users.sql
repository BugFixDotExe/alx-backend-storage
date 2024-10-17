-- A SQL script that creates a table users
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, email VARCHAR(255), name VARCHAR(255), country enum('US', 'CO', 'TN') NOT NULL DEFAULT 'US');
