-- creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE ComputeAverageScoreForUser(IN enter_user_id INT)
BEGIN
    DECLARE c_avg_score FLOAT;
    
    -- Compute average score
    SELECT AVG(score) INTO c_avg_score FROM corrections WHERE user_id = enter_user_id;
    
    -- Update user
    UPDATE users SET average_score = c_avg_score WHERE id = enter_user_id;
END$$

DELIMITER ;
