#!/usr/bin/env python3
'''
A Python function that changes all topics
of a school document based on the name
'''


def update_topics(mongo_collection, name, topics):
    '''
    update_topics: a Python function that changes all
    topics of a school document based on the name
    Args:
        mongo_collection: A mongo collection
        name: (string) will be the school name to update
        topics: (list of strings)will be the list of topics
        approached in the school
    Returns: Nothing.
    '''
    if (mongo_collection.count_documents({}) <= 0):
        return None
    if (isinstance(name, str) is False):
        return None
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
