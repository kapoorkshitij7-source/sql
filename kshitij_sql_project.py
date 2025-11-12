-- Create Database
CREATE DATABASE StudentManagementSystem;
USE StudentManagementSystem;

-- ==========================
-- 1. STUDENTS TABLE
-- ==========================
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    address VARCHAR(255),
    enrollment_date DATE DEFAULT CURRENT_DATE
);

-- ==========================
-- 2. TEACHERS TABLE
-- ==========================
CREATE TABLE Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    department VARCHAR(100)
);

-- ==========================
-- 3. COURSES TABLE
-- ==========================
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    credits INT CHECK (credits >= 1 AND credits <= 6),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- ==========================
-- 4. ENROLLMENTS TABLE
-- ==========================
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
        ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        ON DELETE CASCADE,
    UNIQUE (student_id, course_id) -- prevent duplicate enrollments
);

-- ==========================
-- 5. GRADES TABLE
-- ==========================
CREATE TABLE Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    grade CHAR(2),
    grade_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id)
        ON DELETE CASCADE
);

-- ==========================
-- 6. SAMPLE DATA
-- ==========================

-- Teachers
INSERT INTO Teachers (first_name, last_name, email, department)
VALUES
('John', 'Smith', 'john.smith@school.edu', 'Mathematics'),
('Sarah', 'Lee', 'sarah.lee@school.edu', 'Computer Science');

-- Courses
INSERT INTO Courses (course_name, course_code, credits, teacher_id)
VALUES
('Algebra I', 'MATH101', 3, 1),
('Intro to Programming', 'CS101', 4, 2);

-- Students
INSERT INTO Students (first_name, last_name, date_of_birth, gender, email, phone, address)
VALUES
('Alice', 'Johnson', '2004-03-12', 'Female', 'alice.johnson@example.com', '555-1234', '123 Elm St'),
('Bob', 'Williams', '2003-11-22', 'Male', 'bob.williams@example.com', '555-5678', '456 Oak Ave');

-- Enrollments
INSERT INTO Enrollments (student_id, course_id)
VALUES
(1, 1),
(1, 2),
(2, 2);

-- Grades
INSERT INTO Grades (enrollment_id, grade)
VALUES
(1, 'A'),
(2, 'B+'),
(3, 'A-');

-- ==========================
-- 7. SAMPLE QUERIES
-- ==========================

-- Get all students with their enrolled courses
SELECT s.first_name, s.last_name, c.course_name, g.grade
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
LEFT JOIN Grades g ON e.enrollment_id = g.enrollment_id;

-- List teachers and the courses they teach
SELECT t.first_name AS teacher, c.course_name
FROM Teachers t
JOIN Courses c ON t.teacher_id = c.teacher_id;

-- Find a student's GPA (example logic for numeric conversion)
-- (You'd need a grading scale table for a full implementation)
