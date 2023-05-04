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

