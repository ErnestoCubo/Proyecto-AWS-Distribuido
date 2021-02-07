#!/bin/bash
mysql_install_db --user=root
mysqld --user=root & 
sleep 5
mariadb -e " CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';"
mariadb -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'password';"
mariadb -e "GRANT ALL ON *.* TO 'admin'@'localhost';"
mariadb -e "GRANT ALL ON *.* TO 'admin'@'%';"
mariadb -e "flush privileges;"
mariadb -e "CREATE DATABASE Distribuidos;"
mariadb -D calculadora -e "create table usuarios(email varchar(32), md5 varchar(32));"
mariadb -D calculadora -e "create table resultados(op1 int, op2 int, op3 varchar(5), result int);"
mariadb -D calculadora -e "create table webpages(type varchar(20), pagename varchar(100));"
mariadb -D calculadora -e "insert into  webpages values('success','success.html');"
mariadb -D calculadora -e "commit;"
apachectl -DFOREGROUND
