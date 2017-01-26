# -*- coding: utf-8 -*-
from pymongo import MongoClient

dev = {"ip":"localhost", "port":27017, "database":"warehouse"}

class MongoDatabaseConnector:
	def __init__(self):
		self.ip = dev["ip"]
		self.port = dev["port"]
		self.database = dev["database"]
	
	def getConnection(self):
		self.connection = MongoClient(self.ip, self.port)
		return self.connection
