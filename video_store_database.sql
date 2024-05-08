CREATE DATABASE video_store; #creating a database
USE video_store;			#selecting the database


#creating a table for customers
CREATE TABLE customers_table  	
(custID INT NOT NULL auto_increment,
fname varchar(40) NOT NULL,
sname varchar(40) NOT NULL,
address varchar(40) NOT NULL,
Primary key (custID),
phone varchar(10) NOT NULL UNIQUE);


#creating a table for the videos
CREATE TABLE videos		
(videoID INT NOT NULL auto_increment,
videoVer INT NOT NULL default 1,
vname varchar(15) NOT NULL,
typeq varchar(1) NOT NULL check (typeq= R or B ),
Primary key (videoID),
dateAdded DATEtime  default now());


#creating a table for the hired movies 
Create TABLE hire_table 	
(custID INT NOT NULL default 1,
videoID INT NOT NULL default 1,
videoVer INT  NOT NULL,
dateHired DATE NOT NULL,
c_hireID INT NOT NULL,
v_hireID INT NOT NULL,
FOREIGN KEY (c_hireID) REFERENCES customers_table(custID),
FOREIGN KEY (v_hireID) REFERENCES videos(videoID),
dateReturn DATE);

#inserting data into the hire_table
insert into hire_table(videoVer,dateHired,dateReturn)
values ('1','2023-05-21','2023-05-22'),
('2','2023-05-21','2023-05-22'),
('3','2023-05-22','2023-05-24'),
('1','2023-05-25','2023-05-27'),
('2','2023-05-22','2023-05-29');

#inserting data into the customer table
Insert into customers_table(fname,sname,address,phone)
values ('Vusi','ngumane','97 wildfire avenue','0720791234'),
('stilo','lethwenya','94 steelpark ','0740791751'),
('tido','lethal','9 emza ','0640751754'),
('macklon','miller','450 duncanville','0549763757'),
('John','tylor','48 ali view','0789763755');


#inserting data into the videos table 
Insert into Videos(vname,typeq)
values ('Ponyo','B'),
('Spirited','B'),
('Spirited','B'),
('Mario Brothers','R'),
('Everything','R');








