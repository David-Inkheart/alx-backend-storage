#!/usr/bin/env python3
""" function that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    """ function that provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    numOfdocs = logs_collection.count_documents({})
    print("{} logs".format(numOfdocs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        numOfmethods = logs_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, numOfmethods))
    filter_path = {"method": "GET", "path": "/status"}
    num_path = logs_collection.count_documents(filter_path)
    print("{} status check".format(num_path))

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    ips = logs_collection.aggregate(pipeline)
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
