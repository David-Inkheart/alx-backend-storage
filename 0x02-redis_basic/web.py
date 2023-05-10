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
from functools import wraps


def count_url(method):
    """Decorator to count the number of times a particular URL was accessed"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = "count:" + args[0]
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def cache_page(method):
    """Decorator to cache the result of a particular URL"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = f"data:{args[0]}"
        cached_data = self._redis.get(key)
        if cached_data:
            return cached_data.decode()

        response = requests.get(args[0])
        self._redis.setex(key, 10, response.text)
        return response.text
    return wrapper


_redis = redis.Redis()


@count_url
@cache_page
def get_page(url: str) -> str:
    """Method that returns the HTML content of a particular URL"""
    response = requests.get(url)
    return response.text
