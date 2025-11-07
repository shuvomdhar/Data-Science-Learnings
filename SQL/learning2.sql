CREATE TABLE student (
	Student_id SERIAL PRIMARY KEY,
	Name VARCHAR(100),
	Age BIGINT
);

INSERT INTO student (Name, Age) VALUES
('Aarav Mehta', 20),
('Priya Sharma', 21),
('Rohan Das', 22),
('Isha Mukherjee', 19),
('Karan Patel', 23),
('Sneha Roy', 20),
('Rahul Verma', 21),
('Tanya Sen', 22),
('Arjun Gupta', 24),
('Diya Bose', 19);

SELECT * FROM student;

ALTER TABLE student ADD COLUMN email VARCHAR(100);

ALTER TABLE student DROP COLUMN email;

ALTER TABLE student ADD COLUMN email VARCHAR(100) DEFAULT 'not provided';

ALTER TABLE student RENAME COLUMN Name TO Full_name;

ALTER TABLE student ALTER COLUMN Age TYPE SMALLINT;

ALTER TABLE student ALTER COLUMN Age SET DEFAULT 18;

ALTER TABLE student ALTER COLUMN Age DROP DEFAULT;

ALTER TABLE student ADD CONSTRAINT Age_check CHECK (Age >= 0);

ALTER TABLE student DROP CONSTRAINT Age_check;

ALTER TABLE student RENAME TO school_students;
