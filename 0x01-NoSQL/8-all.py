#!/usr/bin/env python3
'''
A Python function that lists all documents in a collection.
'''


def list_all(mongo_collection):
    '''
    list_all: a function that take a collect and returns it
    Args:
        mongo_collection: A mongo collection
    Returns:
        A collection or an empty list if no document
    '''
    list_of_collections = []
    if (mongo_collection.count_documents({}) <= 0):
        return list_of_collections
    else:
        for document in mongo_collection.find():
            list_of_collections.append(document)
    return list_of_collections
