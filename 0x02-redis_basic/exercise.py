#!/usr/bin/env python3
"""
Creating a cache class that stores data in Redis
"""

import redis
import uuid
from functools import wraps
from typing import Union, Optional, Callable


# count_calls decorator
def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called
    Args:
        method (Callable): Method to count
    Returns:
        Callable: Wrapper function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function
        Returns:
            Callable: Method to count
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

# call_history decorator


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a
    particular function
    Args:
        method (Callable): Method to store history
    Returns:
        Callable: Wrapper function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function
        Returns:
            Callable: Method to store history
        """
        key = method.__qualname__
        input_key = key + ":inputs"
        output_key = key + ":outputs"
        self._redis.rpush(input_key, str(args))
        method_output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, method_output)
        return method_output
    return wrapper


class Cache():
    """Cache class that stores data in Redis
    """

    def __init__(self):
        """Constructor initializes Redis and flushes the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis using a random key

        Args:
            data (can be a str, bytes, int or float): Data to store in Redis

        Returns:
            str: Random key as string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """Get data from Redis and convert it to the desired format

        Args:
            key (str): Key to get from Redis
            fn (Optional[Callable], optional): Function to convert
            data. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: Data converted using fn
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """Convert data to str

        Args:
            key (str): Key to get from Redis

        Returns:
            str: Data as string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """Convert data to int

        Args:
            key (str): Key to get from Redis

        Returns:
            int: Data as int
        """
        return self.get(key, int)

# replay function


def replay(method: Callable):
    """Display the history of calls of a particular function

    Args:
        method (Callable): Method to display history
    """
    r = redis.Redis()
    key = method.__qualname__
    count = r.get(key).decode('utf-8')
    inputs = r.lrange(key + ":inputs", 0, -1)
    outputs = r.lrange(key + ":outputs", 0, -1)
    print("{} was called {} times:".format(key, count))
    for inp, outp in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, inp.decode('utf-8'),
                                     outp.decode('utf-8')))
