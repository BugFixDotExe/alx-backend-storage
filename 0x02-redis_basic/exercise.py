#!/usr/bin/env python3
'''
A Python script that stores an instance
of  a Redis client as a private variable
and flush the instance using the flushdb
'''
import redis


class Cache:
    __init__(self):
        self._redis = redis.Redis()
