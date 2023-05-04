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
- Context: Calculate/compute something is always power intensive… better to distribute the load!


### [**3. Old school band**](./3-glam_rock.sql)
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

- Requirements:
    - Import this table dump: metal_bands.sql.zip
    - Column names must be: band_name and lifespan (in years)
    - You should use attributes formed and split for computing the lifespan
    - Your script can be executed on any database
- Context: Calculate/compute something is always power intensive… better to distribute the load!

### [**4. Buy buy buy**](./4-store.sql)
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

Context: Triggers are very powerful tools to enforce business rules at database level. You can think of them as a way to automatically execute a function when a specific event happens on a specific table.
- Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

### [**5. Email validation to sent**](./5-valid_email.sql)

Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

**Context:** Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

### [**6. Add bonus**](./6-bonus.sql)
Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

Requirements:
- Procedure `AddBonus` takes 3 inputs(in this order):
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    - `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
    - score, the score value for the correction

**Context:** Writing code in SQL is a nice level up!

### [**7. Average score**](./7-average_score.sql)
Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:
- Procedure `ComputeAverageScoreForUser` takes 1 input:
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)

**Context:** Writing code in SQL is a nice level up!

### [**8. Optimize simple search**](./8-index_my_names.sql)
Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

Requirements:
- import this table dump: `names.sql.zip`
- Only the first letter of name must be indexed

**Context:** Indexes are a way to optimize queries execution time. It is a data structure that is used by the database to quickly find a row in a table. Indexes are usually used on columns that are used in WHERE clauses, JOIN clauses or ORDER BY clauses.
- Indexes are not free, they take space on disk and time to be updated when a row is inserted, updated or deleted. You should not index everything, but only the columns that are used in queries.
- Index is not the solution for any performance issue, but when well used, it’s really powerful!

### [**9. Optimize search and score**](./9-index_name_score.sql)

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

Requirements:
- import this table dump: `names.sql.zip`
- Only the first letter of name and score must be indexed

### [**10. Safe divide**](./10-div.sql)
Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:
- You must create a function
- The function `SafeDiv` takes 2 arguments:
    - `a`, INT
    - `b`, INT
- And returns a / b or 0 if b == 0

### [**11. No table for a meeting**](./11-need_meetings.sql)
Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

Requirements:

- The view `need_meeting` should return all students name when:
  - They score are under (strict) to 80
  - AND no `last_meeting` date OR more than a month

**Context:** Views are a way to store a query in the database. It’s a good way to hide complexity and simplify your code. It’s also a good way to reuse a query in multiple places.

### [**12. Average weighted score**](./100-average_weighted_score.sql)

Write a SQL script that creates a function `ComputeAverageWeightedScoreForUser` that computes and store the average weighted score for a student. 

Requirements:
- Procedure `ComputeAverageWeightedScoreForUser` takes 1 input:
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)

### [**13. Average weighted score for all!**](./101-average_weighted_score.sql)

Write a SQL script that creates a function `ComputeAverageWeightedScoreForUsers` that computes and store the average weighted score for all students.

Requirements:

- Procedure `ComputeAverageWeightedScoreForUsers` takes no input
