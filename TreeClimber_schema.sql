DROP DATABASE IF EXISTS TreeClimber;
CREATE DATABASE TreeClimber;
USE TreeClimber;

-- Main course table
CREATE TABLE Courses (
    crn INT PRIMARY KEY,
    course_code VARCHAR(100) NOT NULL,
    department VARCHAR(20),
    course_title VARCHAR(255),
    grad_requirements VARCHAR(50),
    enroll_current INT,
    enroll_max INT,
    enroll_remaining INT
);

-- Meetings table (1-to-many relationship)
CREATE TABLE Meetings (
    meeting_id INT AUTO_INCREMENT PRIMARY KEY,
    crn INT NOT NULL,
    meeting_type VARCHAR(50),
    weekdays VARCHAR(10),
    start_time VARCHAR(10),
    end_time VARCHAR(10),
    class_time VARCHAR(50),
    room VARCHAR(50),

    FOREIGN KEY (crn)
        REFERENCES Courses(crn)
        ON DELETE CASCADE
);