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
import time
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


class Cache:
    """Cache class that stores data in Redis"""

    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_url
    def get_page(self, url: str) -> str:
        """Method that returns the HTML content of a particular URL"""
        key = f"data:{url}"
        cached_data = self._redis.get(key)
        if cached_data:
            return cached_data.decode()

        response = requests.get(url)
        self._redis.setex(key, 10, response.text)
        return response.text

    def get_page_counter(self, url: str) -> int:
        """Method that returns the number of times a particular URL
        was accessed"""
        key = "count:" + url
        return int(self._redis.get(key) or 0)


if __name__ == "__main__":
    cache = Cache()
    url = "https://hub.dummyapis.com/delay?seconds=15"
    for i in range(5):
        start_time = time.time()
        print(f"HTML content of {url}:")
        print(cache.get_page(url))
        print(f"Time taken: {time.time() - start_time:.2f} seconds")
        print(f"Access count for {url}: {cache.get_page_counter(url)}")
        print("----------------------")
        time.sleep(2)  # wait for 2 seconds between requests
