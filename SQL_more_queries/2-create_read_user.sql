-- create read user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
-- GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost