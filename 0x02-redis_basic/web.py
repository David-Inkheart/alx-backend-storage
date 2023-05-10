#!/usr/bin/env python3
"""
In this tasks, we will implement a `get_page` function
(prototype: def get_page(url: str) -> str:).
The core of the function is very simple. It uses the `requests`
module to obtain the HTML content of a particular URL and returns it.

Start in a new file named `web.py` and do not reuse the code written
in `exercise.py`.

Inside `get_page` track how many times a particular URL was
accessed in the key "count:{url}" and cache the result with an
expiration time of 10 seconds.

Tip: Use `http://slowwly.robertomurray.co.uk` to simulate a slow
response and test your caching.

Bonus: implement this use case with decorators.
"""

import redis
import requests
from typing import Callable


_redis = redis.Redis()


def count_access(func: Callable) -> Callable:
    """
    Counts the number of times
    a url was accessed
    """
    def wrapper(*args, **kwargs):
        """wrapper"""
        key = "count:{}".format(args[0])
        _redis.incr(key)
        return func(*args, **kwargs)
    return wrapper


def get_cache(func: Callable) -> Callable:
    """
    Counts the number of times
    a url was accessed
    """
    def wrapper(*args, **kwargs):
        """wrapper"""
        key = "result:{}".format(args[0])
        if _redis.exists(key):
            data = _redis.get(key)
            return data.decode('utf-8')
        return func(*args, **kwargs)
    return wrapper


@get_cache
@count_access
def get_page(url: str) -> str:
    """
    Obtains the HTML content of a
    particular URL and returns it
    """
    key = "result:{}".format(url)

    response = requests.get(url)

    _redis.set(key, response.text, ex=10)

    return response.text
