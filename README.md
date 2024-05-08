# SQL-DATA-FRAMEWORK
creating an SQL framework to store Game Data

## Contents
1. [Description of application](#description-of-application)
2. [Installation and setup](#installation-and-setup)
3. [How to use the application](#how-to-use-the-application)
4. [How to handle errors](#how-to-handle-errors)
5. [MySQL database](#mysql-database)
6. [Application Server](#application-server)
7. [Application Client](#application-client)
8. [Screenshots of application](#screenshots-of-application)

## Description of application
A video store system developed to manage customer records and video inventory. The system consists of server and client-side applications. The server connects to a MySQL database named `video_store`. Customers must register before renting videos.

## Installation and setup
To set up the application:
- Install MySQL and Python.
- Create a `video_store` database using MySQL Workbench.
- Establish a connection between the server application and MySQL using MySQL Connector.
- Ensure Python has MySQL drivers installed.
- Install PIP to install MySQL Connector.

## How to use the application
1. **Customer Registration**:
   - Users register with their phone numbers.
   - If not existing, users provide name, surname, and address.
2. **Movie Registration**:
   - Users register movies with name and type (new or old).
   - Movie versions increase if the same name is registered.
3. **Renting a Movie**:
   - Users provide phone number and video ID to rent.
   - Rental date is automated to the current date.
4. **Returning a Movie**:
   - Users provide the video ID to return.
   - Rental status is updated.

## How to handle errors
- Ensure correct details are entered during customer registration.
- Verify the selected movie during registration.

## MySQL database
```sql
-- Create database
CREATE DATABASE video_store;

-- Create customers table
CREATE TABLE customers_table (
    custID INT NOT NULL auto_increment,
    fname varchar(40) NOT NULL,
    sname varchar(40) NOT NULL,
    address varchar(40) NOT NULL,
    Primary key (custID),
    phone varchar(10) NOT NULL UNIQUE
);

-- Create videos table
CREATE TABLE videos (
    videoID INT NOT NULL auto_increment,
    videoVer INT NOT NULL default 1,
    vname varchar(15) NOT NULL,
    typeq varchar(1) NOT NULL check (typeq= 'R' or typeq= 'B' ),
    Primary key (videoID),
    dateAdded DATETIME default now()
);

-- Create hire table
CREATE TABLE hire_table (
    custID INT NOT NULL default 1,
    videoID INT NOT NULL default 1,
    videoVer INT  NOT NULL,
    dateHired DATE NOT NULL,
    c_hireID INT NOT NULL,
    v_hireID INT NOT NULL,
    FOREIGN KEY (c_hireID) REFERENCES customers_table(custID),
    FOREIGN KEY (v_hireID) REFERENCES videos(videoID),
    dateReturn DATE
);

-- Insert data into tables (customers, videos, hire_table)
-- (Data insertion statements provided in the original script)

# Server script provided in the original script
# (Python server script for handling client requests)
# Client script provided in the original script
# (Python client script for interacting with the server)


