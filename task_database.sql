DROP DATABASE IF EXISTS task_database;
CREATE DATABASE task_database;
USE task_database;

CREATE TABLE tasks (
p_id INT AUTO_INCREMENT PRIMARY KEY,
p_task_name VARCHAR(255) NOT NULL,
p_completed BOOLEAN DEFAULT FALSE,
p_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

DELIMITER //
CREATE PROCEDURE sp_get_tasks()
BEGIN 
	SELECT p_id, p_task_name, p_completed, p_created_at 
    FROM tasks;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_add_tasks(IN p_task_name VARCHAR(255), IN p_completed BOOLEAN)
BEGIN
	INSERT INTO tasks (p_task_name, p_completed) VALUES (p_task_name, p_completed);
END //

DELIMITER ;

SHOW DATABASES;

call sp_add_tasks();

INSERT INTO tasks (p_task_name, p_completed) VALUES ('Sample Task 1', false);
INSERT INTO tasks (p_task_name, p_completed) VALUES ('Sample Task 2', true);

SELECT * FROM tasks;
