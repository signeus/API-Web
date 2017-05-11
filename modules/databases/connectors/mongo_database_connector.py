# -*- coding: utf-8 -*-
from pymongo import MongoClient

class MongoDatabaseConnector:
	def __init__(self, resourceManagerParameters):
		self.ip = resourceManagerParameters["ip_database"]
		self.port = int(resourceManagerParameters["port_database"])
		self.database = resourceManagerParameters["name_database"]
	
	def getConnection(self):
		self.connection = MongoClient(self.ip, self.port)
		return self.connection
