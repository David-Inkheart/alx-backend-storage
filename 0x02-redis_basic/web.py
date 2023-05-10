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
from typing import Callable


redis_client = redis.Redis()


def cache_page(time: int):
    """
    Decorator to cache the result of a particular URL
    with expiration time
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            """Wrapper function"""
            cache_key = f"data:{url}"
            cached_data = redis_client.get(cache_key)
            if cached_data:
                return cached_data.decode()
            response = func(url)
            redis_client.setex(cache_key, time, response)
            return response
        return wrapper
    return decorator


def count_url(func: Callable) -> Callable:
    """Decorator to count the number of times a particular URL was accessed"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """Wrapper function"""
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url)
    return wrapper


@cache_page(10)
@count_url
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and return it"""
    response = requests.get(url)
    return response.text
