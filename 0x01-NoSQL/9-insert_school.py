#!/usr/bin/env python3
'''
 a Python script that inserts a new document
 in a collection based on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''
    insert_school: a function that insers a new doc in a collection
    based on the kwargs
    Args:
        mongo_collection: A mongodb collection objects
        kwargs: a Python **kwargs dict.
    Returns:
        A new _id
    '''
    if (mongo_collection.count_documents({}) <= 0):
        return None
    if (kwargs is None or len(kwargs) == 0):
        return None
    else:
        added_item = mongo_collection.insert_one(kwargs)
        if added_item is not None:
            return added_item.inserted_id

