
create database retail;
use retail;

show databases;
CREATE TABLE salespeople (
         snum    INT  NOT NULL,
         sname VARCHAR(30)   NOT NULL,
         city  VARCHAR(30)   NOT NULL,
         comm  DECIMAL(4,2)  NOT NULL,
         PRIMARY KEY  (snum)
       );
INSERT INTO salespeople VALUES (1001, 'Peel', 'London', 0.12);
INSERT INTO salespeople VALUES (1002, 'Serres', 'San Jose', .13);
INSERT INTO salespeople VALUES (1004,'Motika', 'London', .11);
INSERT INTO salespeople VALUES (1007,'Rifkin', 'Barcelona', .15);
INSERT INTO salespeople VALUES (1003,'AxelRod', 'New York', .10);
INSERT INTO salespeople VALUES (1005,'Fran', 'London', .26);
CREATE TABLE customer (
         cnum    INT  NOT NULL,
         cname VARCHAR(30)   NOT NULL,
         city  VARCHAR(30)   NOT NULL,
         rating int not null,
         snum  int  NOT NULL,
         PRIMARY KEY  (cnum),
     FOREIGN KEY (snum) REFERENCES salespeople(snum));

INSERT INTO customer VALUES (2001, 'Hoffman', 'London',100, 1001);
INSERT INTO customer VALUES (2002,'Giovanni', 'Rome', 200, 1003);
INSERT INTO customer VALUES (2003,'Liu','San Jose',200,1002);
INSERT INTO customer VALUES (2004,'Grass', 'Berlin', 300,1002);
INSERT INTO customer VALUES (2006,'Clemens', 'London', 100, 1001);
INSERT INTO customer VALUES(2008,'Cisneros','San Jose',300, 1007);
INSERT INTO customer VALUES (2007,'Pereira', 'Rome', 100 ,1004);

select * from customer;


CREATE TABLE orders ( 
         onum    INT  NOT NULL, 
    amt  DECIMAL(7,2)  NOT NULL, 
         odate  Date   NOT NULL, 
 cnum  int  NOT NULL, 
         PRIMARY KEY  (onum), 
     FOREIGN KEY (cnum) REFERENCES customer(cnum) 
       ); 

INSERT INTO orders VALUES (3001, 18.69, '1996-03-10', 2008);
INSERT INTO orders VALUES (3003, 767.19, '1996-10-03', 2001);  
INSERT INTO orders VALUES (3002, 1900.10, '1996-10-03', 2007);  
INSERT INTO orders VALUES (3005, 5160.45, '1996-10-03', 2003);  
INSERT INTO orders VALUES (3006, 1098.16, '1996-10-03', 2008);  
INSERT INTO orders VALUES (3009, 1713.23, '1996-10-04', 2002);  
INSERT INTO orders VALUES (3007, 75.75, '1996-10-04', 2002);  
INSERT INTO orders VALUES (3008, 4723.00, '1996-10-05', 2006);  
INSERT INTO orders VALUES (3010, 1309.95, '1996-10-06', 2004);  
INSERT INTO orders VALUES (3011, 9891.88, '1996-10-06', 2006);  

