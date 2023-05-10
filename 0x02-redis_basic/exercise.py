#!/usr/bin/env python3
"""
Creating a cache class that stores data in Redis
"""

import redis
import uuid


class Cache():
    """Cache class that stores data in Redis
    """

    def __init__(self):
        """Constructor initializes Redis and flushes the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    # def store(self, data: Union[str, bytes, int, float]) -> str:
    def store(self, data: str | bytes | int | float) -> str:
        """Store data in Redis using a random key

        Args:
            data (can be a str, bytes, int or float): Data to store in Redis

        Returns:
            str: Random key as string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
