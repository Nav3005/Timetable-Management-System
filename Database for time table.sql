CREATE DATABASE timetable_db;
USE timetable_db;
CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept VARCHAR(50) NOT NULL
);
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    mne VARCHAR(10) NOT NULL,
    teacher_id INT,
    periods_as_per_syllabus INT NOT NULL,
    allotted_periods INT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);
CREATE TABLE timetable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    day VARCHAR(10) NOT NULL,
    time_slot VARCHAR(20) NOT NULL,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);