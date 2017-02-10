# -*- coding: utf-8 -*-
from connectors.mongo_database_connector import MongoDatabaseConnector

class MongoDatabaseManager:
	def __init__(self, resourceManagerParameters):
		self.rm = resourceManagerParameters

	def connect2Database(self):
		self.con = MongoDatabaseConnector(self.rm).getConnection()
		self.db = self.con[self.rm["name_database"]]
		return self.db
