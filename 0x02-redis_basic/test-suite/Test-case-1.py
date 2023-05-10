#!/usr/bin/env python3
"""
Test file 1
The following code should not raise:
"""

Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
print("")
print("OK")
print("-----------------------------------")
print("Test Case 1 Passed")
