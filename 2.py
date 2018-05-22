CREATE DATABASE mine;

USE mine;

CREATE TABLE family
(
 family_name varchar(15) NOT NULL,
 sur_name varchar(10) NOT NULL,
 age int 
 
 );
 
 
 ALTER TABLE family ADD (population int);
 desc family;
 
 alter table family drop age;
 
 desc family;
  
 TRUNCATE table family;
