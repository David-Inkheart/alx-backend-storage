#!/usr/bin/env python3
"""
Creating a cache class that stores data in Redis
"""

import redis
import uuid
from typing import Union, Optional, Callable


class Cache():
    """Cache class that stores data in Redis
    """

    def __init__(self):
        """Constructor initializes Redis and flushes the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
