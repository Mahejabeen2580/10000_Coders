create database college;
show databases;
use college;--
create table students(Student_ID int primary key,Student_name varchar(50) NOT NULL , Email_ID varchar(100) unique ,Age int check(Age>=18)
 , Is_Active bool default True );
describe students;
create table Enrollment(Enrollment_ID int primary key, course_name varchar(10) unique not null,credits int check(credits between 1 and 5)
,Student_ID int ,foreign key(Student_ID) references students(Student_ID),Enrollment_Date date default (current_date()));
describe Enrollment;
insert into students(Student_ID ,Student_name,Email_ID,Age) values(606,'Rahel','rachl9926@gmail.com',19),(899,'Aliza','alizey711@gmail.com',22)
,(649,'Nail','nailstruxx02@gmail.com',19);
select*from students;
insert into Enrollment(Enrollment_ID ,course_name,credits ,Student_ID) values(08994,'PythonDA',2,606),
(08995,'DataDA',3,899),(08996,'Java',4,649);
select*from Enrollment;
