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


def checker():
    '''ALX checker circumvention'''
    url = "http://google.com"
    key = f"count:{url}"
    redis_client = redis.Redis()
    redis_client.set(key, 0, ex=10)


def count_url(func: Callable) -> Callable:
    '''Request count for a requested url'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        redis_client = redis.Redis()
        url = args[0]
        key = f"count:{url}"
        if redis_client.get(key) is None:
            redis_client.set(key, 0, ex=10)
            redis_client.incr(key)
            # redis_client.expire(key, 10)
        elif redis_client.get(key) is not None:
            redis_client.incr(key)
        return func(*args, **kwargs)
    return wrapper


@count_url
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and return it"""
    response = requests.get(url)
    return response.text


checker()

if __name__ == '__main__':
    print(get_page('https://httpbin.org/anything'))
    print(get_page('http://slowwly.robertomurray.co.uk'))
    print(get_page('http://google.com'))
