CREATE DATABASE new_db;

CREATE TABLE student;

INSERT INTO student (name, age, grad)
VALUES ('Shuvom', 22, 'A'),
		('Anjali', 21, 'B');

SELECT * FROM student;

SELECT name FROM student;

SELECT name FROM student WHERE age=23;

UPDATE student SET age=24 WHERE name='Shuvom';

UPDATE student SET student_id=1 WHERE name='Anjali';

UPDATE student SET student_id=2 WHERE name='Shuvom';

DELETE FROM student WHERE name='Anjali';



CREATE TABLE numbers (
	Id serial,
	Age smallint,
	Price numeric(4, 2),
	Rating real
);

INSERT INTO numbers (Age, Price, Rating) VALUES (23, 23.67, 12.567);

INSERT INTO numbers (Age, Price, Rating) VALUES (12, 20.79, 5.5797);

SELECT * FROM numbers;



CREATE TABLE strings (
	Code char(5),
	Email varchar(100),
	Bio text
);

INSERT INTO strings VALUES ('23vb4', 'doe.john@gmail.com', 'Hi, I am a Developer and I am good with AI');

SELECT * FROM strings;

ALTER TABLE strings ADD COLUMN S_active boolean;



CREATE TABLE random (
	Id serial primary key,
	Name varchar(100) not null,
	Email varchar(100) unique not null,
	Created_at date default now(),
	Age int check (age>=18)
);

INSERT INTO random (Name, Email, Age) 
VALUES ('Shuvom', 'dhar.shuvom@gmail.com', 23);

SELECT * FROM random;



-- Practice
CREATE DATABASE Flipkart_db;
