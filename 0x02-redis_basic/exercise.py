#!/usr/bin/env python3
'''
A Python script that stores an instance
of  a Redis client as a private variable
and flush the instance using the flushdb
'''
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    '''
    class (Cache): a class that serves as the blueprint for
    all other redis instances
    '''
    def __init__(self):
        '''
        __init__: a constructor to Cache
        Args: self
        Properties:
            self._redis: a private variable
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store: a function that returns the uuid key for th db obj
        Args: data the input data of types str, bytes, int, float
        Returns:
            returns the key assigned to the data in the redis db
        '''
        key = f'{uuid.uuid4()}'
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]):
        value = self._redis.get(key)
        if value is None:
            return None

        if fn is None:
            return value
        if 'int' in str(fn):
            return self.get_int(value)
        if 'function' in str(fn):
            return self.get_str(value)

    def get_str(self, value):
        return value.decode('utf-8')

    def get_int(self, value):
        return int(value)
