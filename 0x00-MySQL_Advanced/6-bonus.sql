-- creates a stored procedure AddBonus that adds a new correction for a student.
-- The procedure first checks if a project with the given `project_name`
-- already exists in the projects table. If not, it creates a new project
-- with the given project_name and retrieves its ID using the
-- LAST_INSERT_ID() function.
-- Finally, the procedure inserts a new correction into the corrections table,
-- with the given user_id, the project_id of the project
-- (either retrieved or inserted in the previous step), and the given score.

-- To call this procedure, you can simply use the following SQL statement:
-- CALL AddBonus(user_id, project_name, score);
DELIMITER $$

DROP PROCEDURE IF EXISTS AddBonus;

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Check if project already exists?
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    -- if it does not, insert new project
    IF project_id IS NULL THEN
	INSERT INTO projects (name) VALUES (project_name);
	SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert new correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END$$
DELIMITER ;
