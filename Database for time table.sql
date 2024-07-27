CREATE DATABASE timetable_db; -- Creation of Database
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

                   -- Insertion of values 
 
INSERT INTO teachers (name, dept) VALUES -- Teachers table 
('Alice Smith', 'Mathematics'),
('Bob Johnson', 'Physics'),
('Charlie Brown', 'Chemistry'),
('David Wilson', 'Biology'),
('Eve Davis', 'English');

INSERT INTO subjects (code, name, mne, teacher_id, periods_as_per_syllabus, allotted_periods) VALUES -- Subject Table 
('MATH101', 'Calculus', 'CAL', 1, 4, 4),
('PHYS101', 'Mechanics', 'MEC', 2, 4, 4),
('CHEM101', 'Organic Chemistry', 'ORG', 3, 4, 4),
('BIO101', 'General Biology', 'BIO', 4, 4, 4),
('ENG101', 'English Literature', 'LIT', 5, 4, 4);

INSERT INTO timetable (day, time_slot, subject_id) VALUES -- Timetable table 
('MON', '8.15-9.05 AM', 1),
('MON', '9.05-9.55 AM', 2),
('MON', '10.10-11.00 AM', 3),
('MON', '11.00-11.50 AM', 4),
('MON', '11.50-12.40 PM', 5),
('MON', '1.30-2.15 PM', 1),
('MON', '2.15-3.00 PM', 2),
('MON', '3.00-3.45 PM', 3),
('MON', '4.00-5.00 PM', 4),
('TUE', '8.15-9.05 AM', 5),
('TUE', '9.05-9.55 AM', 1),
('TUE', '10.10-11.00 AM', 2),
('TUE', '11.00-11.50 AM', 3),
('TUE', '11.50-12.40 PM', 4),
('TUE', '1.30-2.15 PM', 5),
('TUE', '2.15-3.00 PM', 1),
('TUE', '3.00-3.45 PM', 2),
('TUE', '4.00-5.00 PM', 3),
('WED', '8.15-9.05 AM', 4),
('WED', '9.05-9.55 AM', 5),
('WED', '10.10-11.00 AM', 1),
('WED', '11.00-11.50 AM', 2),
('WED', '11.50-12.40 PM', 3),
('WED', '1.30-2.15 PM', 4),
('WED', '2.15-3.00 PM', 5),
('WED', '3.00-3.45 PM', 1),
('WED', '4.00-5.00 PM', 2),
('THU', '8.15-9.05 AM', 3),
('THU', '9.05-9.55 AM', 4),
('THU', '10.10-11.00 AM', 5),
('THU', '11.00-11.50 AM', 1),
('THU', '11.50-12.40 PM', 2),
('THU', '1.30-2.15 PM', 3),
('THU', '2.15-3.00 PM', 4),
('THU', '3.00-3.45 PM', 5),
('THU', '4.00-5.00 PM', 1),
('FRI', '8.15-9.05 AM', 2),
('FRI', '9.05-9.55 AM', 3),
('FRI', '10.10-11.00 AM', 4),
('FRI', '11.00-11.50 AM', 5),
('FRI', '11.50-12.40 PM', 1),
('FRI', '1.30-2.15 PM', 2),
('FRI', '2.15-3.00 PM', 3),
('FRI', '3.00-3.45 PM', 4),
('FRI', '4.00-5.00 PM', 5);
