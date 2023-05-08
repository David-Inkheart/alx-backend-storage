# This project covers some advanced MySQL topics such as:
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL


# Tasks

### [**0. We are all unique!**](./0-uniq_users.sql)
Write a SQL script that creates a table users following these requirements:

- With these attributes:
    - id, integer, never null, auto increment and primary key
    - email, string (255 characters), never null and unique
    - name, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database

**Context**: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application

### [**1. In and not out**](./1-country_users.sql)
Write a SQL script that creates a table users following these requirements:

- With these attributes:
    - id, integer, never null, auto increment and primary key
    - email, string (255 characters), never null and unique
    - name, string (255 characters)
    - country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
- If the table already exists, your script should not fail
- Your script can be executed on any database

**Context**: An enumeration is a list of strings limited to a set of possible values. It is a data type that is not part of the SQL standard and is offered by MySQL.

### [**2. Best band ever!**](./2-fans.sql)
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

- Requirements:
    - Import this table dump: metal_bands.sql.zip
    - Column names must be: origin and nb_fans
    - Your script can be executed on any database
**Context:** Calculate/compute something is always power intensive… better to distribute the load!

-- Solution to above question

SELECT origin, sum(fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;

### [**3. Old school band**](./3-glam_rock.sql)
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

- Requirements:
    - Import this table dump: metal_bands.sql.zip
    - Column names must be: band_name and lifespan (in years)
    - You should use attributes formed and split for computing the lifespan
    - Your script can be executed on any database
**Context:** Calculate/compute something is always power intensive… better to distribute the load!

-- Solution to above question

SELECT band_name, 
    CASE WHEN split is NULL THEN 2022 - formed
    ELSE split - formed END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

### [**4. Buy buy buy**](./4-store.sql)
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

**Context:** Triggers are very powerful tools to enforce business rules at database level. You can think of them as a way to automatically execute a function when a specific event happens on a specific table.
- Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

-- Solution to above question

DELIMITER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$
DELIMITER ;


### [**5. Email validation to sent**](./5-valid_email.sql)

Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

**Context:** Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

-- Solution to above question

DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email
        AND NEW.email REGEXP '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
        THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;

### [**6. Add bonus**](./6-bonus.sql)
Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

Requirements:
- Procedure `AddBonus` takes 3 inputs(in this order):
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    - `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
    - score, the score value for the correction

**Context:** Writing code in SQL is a nice level up!

-- Solution to above question

DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    
    -- Check if project already exists, otherwise insert new project
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    
    -- Insert new correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$
DELIMITER ;

### [**7. Average score**](./7-average_score.sql)
Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:
- Procedure `ComputeAverageScoreForUser` takes 1 input:
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)

**Context:** Writing code in SQL is a nice level up!

-- Solution to above question

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(3,2);
    
    -- Compute average score
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
    
    -- Update user
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END$$
DELIMITER ;

### [**8. Optimize simple search**](./8-index_my_names.sql)
Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

Requirements:
- import this table dump: `names.sql.zip`
- Only the first letter of name must be indexed

**Context:** Indexes are a way to optimize queries execution time. It is a data structure that is used by the database to quickly find a row in a table. Indexes are usually used on columns that are used in WHERE clauses, JOIN clauses or ORDER BY clauses.
- Indexes are not free, they take space on disk and time to be updated when a row is inserted, updated or deleted. You should not index everything, but only the columns that are used in queries.
- Index is not the solution for any performance issue, but when well used, it’s really powerful!

-- Solution to above question

CREATE INDEX idx_name_first ON names (name(1));

### [**9. Optimize search and score**](./9-index_name_score.sql)

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

Requirements:
- import this table dump: `names.sql.zip`
- Only the first letter of name and score must be indexed

-- Solution to above question

CREATE INDEX idx_name_first_score ON names (name(1), score);

### [**10. Safe divide**](./10-div.sql)
Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:
- You must create a function
- The function `SafeDiv` takes 2 arguments:
    - `a`, INT
    - `b`, INT
- And returns a / b or 0 if b == 0

**Context:** Writing code in SQL is a nice level up!

-- Solution to above question

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$
DELIMITER ;

### [**11. No table for a meeting**](./11-partition_meetings.sql)
Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

Requirements:

- The view `need_meeting` should return all students name when:
  - They score are under (strict) to 80
  - AND no `last_meeting` date OR more than a month