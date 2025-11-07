CREATE TABLE students (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(100)
);

INSERT INTO students (student_id, student_name)
VALUES (1, 'Akarsh'),
       (2, 'Simran'),
	   (3, 'Rohan');

SELECT * FROM students;

CREATE TABLE courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(100)
);

INSERT INTO courses (course_id, course_name)
VALUES (101, 'Python'),
       (102, 'SQL'),
	   (103, 'Power BI');

SELECT * FROM courses;

CREATE TABLE student_courses (
  student_id INT,
  course_id INT,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Sample Mapping
INSERT INTO student_courses (student_id, course_id) VALUES
(1, 101), (1, 102), (2, 101), (2, 103), (3, 102);

SELECT * FROM student_courses;

SELECT s.student_name, c.course_name
FROM student_courses sc
JOIN students s ON sc.student_id = s.student_id
JOIN courses c ON sc.course_id = c.course_id;

SELECT c.course_name
FROM student_courses sc
JOIN students s ON sc.student_id = s.student_id
JOIN courses c ON sc.course_id = c.course_id
WHERE s.student_name = 'Simran';
