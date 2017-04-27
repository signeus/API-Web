# -*- coding: utf-8 -*-
from pymongo import MongoClient

class MongoLogDatabaseConnector:
    def __init__(self, resourceManagerParameters):
        self.ip = resourceManagerParameters["ip_log_database"]
        self.port = int(resourceManagerParameters["port_log_database"])
        self.database = resourceManagerParameters["name_log_database"]

    def getConnection(self):
        self.connection = MongoClient(self.ip, self.port)
        return self.connection
