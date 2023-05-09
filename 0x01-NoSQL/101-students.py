#!/usr/bin/env python3
""" function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """ function that returns all students sorted by average score"""
    pipeline = [
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    cursor = mongo_collection.aggregate(pipeline)
    for document in cursor:
        yield document
