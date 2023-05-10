## This project covers how to use Redis for basic operations and as a caching system

# TASKS

### [0. Writing strings to Redis](./exercise_0.py)
Create a `Cache` class. In the `__init__` method, store an instance of the `Redis client` as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using flushdb.

Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.

Type-annotate `store` correctly. Remember that data can be a str, bytes, int or float.
```
bob@dylan:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
bob@dylan:~$ 
```