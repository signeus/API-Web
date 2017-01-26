# -*- coding: utf-8 -*-
from connectors.mongo_database_connector import MongoDatabaseConnector

class MongoDatabaseManager:
	
	def connect2Database(self, database):
		self.con = MongoDatabaseConnector().getConnection()
		self.db = self.con[database]
		return self.db
