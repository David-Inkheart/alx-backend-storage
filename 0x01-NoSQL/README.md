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

### [2. Insert document](./2-insert)
Write a script that inserts a document in the collection `school`:
- The document must have one attribute `name` with value “Holberton school”
- The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 2-insert | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
guillaume@ubuntu:~/0x01$
```

### [3. All documents](./3-all)
Write a script that lists all documents in the collection `school`:
- The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 3-all | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```

### [4. All matches](./4-match)

Write a script that lists all documents with `name="Holberton school"` in the collection `school`:
- The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```

### [5. Count](./5-count)

Write a script that displays the number of documents in the collection `school`:
- The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 5-count | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
1
bye
guillaume@ubuntu:~/0x01$
```

### [6. Update](./6-update)

Write a script that adds a new attribute to a document in the collection `school`:
- The script should update only document with `name="Holberton school"` (all of them)
- The update should add the attribute `address` with the value “972 Mission street”
- The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 6-update | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
guillaume@ubuntu:~/0x01$ 
```

### [7. Delete by match](./7-delete)

Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:
- The database name will be passed as option of mongo command

```
guillaume@ubuntu:~/0x01$ cat 7-delete | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "acknowledged" : true, "deletedCount" : 1 }
bye
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
bye
guillaume@ubuntu:~/0x01$ 
```

### [8. List all documents in Python](./8-all.py)

Write a Python function that lists all documents in a collection:
- Prototype: `def list_all(mongo_collection):`
- Return an empty list if no document in the collection
- `mongo_collection` will be the `pymongo` collection object

```
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ ./8-main.py
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
guillaume@ubuntu:~/0x01$ 
```

### [9. Insert a document in Python](./9-insert_school.py)

Write a Python function that inserts a new document in a collection based on `kwargs`:
- Prototype: `def insert_school(mongo_collection, **kwargs):`
- `mongo_collection` will be the `pymongo` collection object
- Returns the new `_id`

```
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ ./9-main.py
New school created: 5a8f60cfd4321e1403ba7abb
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
[5a8f60cfd4321e1403ba7abb] UCSF 505 Parnassus Ave
```

### [10. Change school topics](./10-update_topics.py)

Write a Python function that changes all topics of a school document based on the name:
- Prototype: `def update_topics(mongo_collection, name, topics):`
- `mongo_collection` will be the `pymongo` collection object
- `name` (string) will be the school name to update
- `topics` (list of strings) will be the list of topics approached in the school

```
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ ./10-main.py
[5a8f60cfd4321e1403ba7abb] UCSF 
[5a8f60cfd4321e1403ba7aba] UCSD 
[5a8f60cfd4321e1403ba7ab9] Holberton school ['Sys admin', 'AI', 'Algorithm']
[5a8f60cfd4321e1403ba7abb] UCSF 
[5a8f60cfd4321e1403ba7aba] UCSD 
[5a8f60cfd4321e1403ba7ab9] Holberton school ['iOS']
guillaume@ubuntu:~/0x01$ 
```

### [11. Where can I learn Python?](./11-schools_by_topic.py)

Write a Python function that returns the list of school having a specific topic:
- Prototype: `def schools_by_topic(mongo_collection, topic):`
- `mongo_collection` will be the `pymongo` collection object
- `topic` (string) will be topic searched

```
guillaume@ubuntu:~/0x01$ 
guillaume@ubuntu:~/0x01$ ./11-main.py
[5a90731fd4321e1e5a3f53e3] Holberton school ['Algo', 'C', 'Python', 'React']
[5a90731fd4321e1e5a3f53e5] UCLA ['C', 'Python']
guillaume@ubuntu:~/0x01$ 
```