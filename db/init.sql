CREATE DATABASE team_data;
USE team_data;

CREATE TABLE  team_members (
    student_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    cgpa DECIMAL(4, 2) NOT NULL
);

INSERT INTO team_members (name, student_id, age, cgpa) VALUES
('Omar Refaee Refaee', '22010165', 20, 3.12),
('Mohammed Yasser Elkoutp', '22010234', 20, 3.566),
('MennatAllah Moamen Madany', '22012051', 20, 3.67),
('Salma Shehab Eldeen Ahmed', '22011563', 20, 3.89),
('Hossam Hasan Ahmed', '20201497622', 20, 3.75);

