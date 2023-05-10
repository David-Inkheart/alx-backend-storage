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
from functools import wraps

redis = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """ Decorator wrapper """

    @wraps(fn)
    def wrapper(url):
        """ Wrapper for decorator guy """
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """get page self descriptive
    """
    response = requests.get(url)
    return response.text
