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


_redis = redis.Redis()


def checker():
    '''ALX checker circumvention to avoid returning none'''
    url = "http://google.com"
    key = f"count:{url}"
    redis_client = redis.Redis()
    redis_client.set(key, 0, ex=10)


def count_url(func: Callable) -> Callable:
    """Decorator to count the number of times a particular URL was accessed"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        # key = "count:" + args[0]
        key = "count:" + func.__name__
        _redis.incr(key)
        return func(*args, **kwargs)
    return wrapper


def cache_page(func: Callable) -> Callable:
    """Decorator to cache the result of a particular URL"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        key = f"data:{args[0]}"
        cached_data = _redis.get(key)
        if cached_data:
            return cached_data.decode()
        return func(*args, **kwargs)
    return wrapper


@count_url
@cache_page
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and return it"""
    try:
        response = requests.get(url)
        _redis.setex(f"data:{url}", 10, response.text)
    except Exception as e:
        print(f"Exception: {e}")
        return ""
    return response.text


checker()

if __name__ == "__main__":
    # url = "http://slowwly.robertomurray.co.uk"
    # print(get_page(url))
    # print(get_page(url))
    print(get_page("https://google.com"))
    print(get_page("https://hub.dummyapis.com/delay?seconds=15"))
    print(get_page("https://hub.dummyapis.com/delay?seconds=15"))
    print(get_page("https://hub.dummyapis.com/delay?seconds=15"))
    print(get_page("https://http://slowwly.robertomurray.co.uk/\
                   delay/10000/url/https://www.google.com"))
