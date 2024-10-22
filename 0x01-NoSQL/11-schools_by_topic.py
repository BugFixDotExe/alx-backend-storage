#!/usr/bin/env python3
'''
A Python script that returns
the list of school having a
specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    schools_by_topic:  a Python function that
    returns the list of school having a specific topic
    Args:
        mongo_collection: a pymongo collection object
        topic:  (string) will be topic searched
    Returns:
        returns the list of school having a specific topic.
    '''
    ret_obj = []
    if (isinstance(topic, str) is False or len(topic) == 0):
        return None
    else:
        for doc in mongo_collection.find({}):
            single_topic = doc.get('topics')
            if single_topic is not None:
                if topic in single_topic:
                    ret_obj.append(doc)
    return ret_obj
