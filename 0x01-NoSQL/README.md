## This project covers NoSQL topics and concepts:

- What NoSQL means
- The difference between SQL and NoSQL
- ACID
- Document storage
- NoSQL types
- Benefits of a NoSQL database
- Querying information from a NoSQL database
- Insert/update/delete information from a NoSQL database
- Using MongoDB

# TASKS

### [0. List all databases](./0-list_databases)
Write a script that lists all databases in MongoDB.
```
guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
```

### [1. Create a database](./1-use_or_create_database)
Write a script that creates or uses the database my_db:
```
guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
guillaume@ubuntu:~/0x01$ cat 1-use_or_create_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
guillaume@ubuntu:~/0x01$
```