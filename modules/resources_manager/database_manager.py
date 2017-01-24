# -*- coding: utf-8 -*-
from pymongo import MongoClient
from pymongo.collection import ReturnDocument

class DatabaseManager:
	def connect2Database(self, ip, port, database):
		self.connection = MongoClient(ip, port)
		self.db = connection[database]
		return self.db

	def openCollection(self, collection):
		self.collection = self.db[collection]
		return self.collection

	def insert2Collection(self, collection, data):
		result = self.collection.insert(data)
		return result
