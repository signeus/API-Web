# -*- coding: utf-8 -*-
from connectors.mongo_database_connector import MongoDatabaseConnector
from connectors.mongo_log_database_connector import MongoLogDatabaseConnector

class MongoDatabaseManager:
	def __init__(self, resourceManagerParameters):
		self.rm = resourceManagerParameters

	def connect2Database(self):
		self.con = MongoDatabaseConnector(self.rm).getConnection()
		self.con.kayoo.authenticate(self.rm["user_database"], self.rm["psswd_database"], mechanism='SCRAM-SHA-1')
		self.db = self.con[self.rm["name_database"]]
		return self.db

	def connect2LogDatabase(self):
		self.con = MongoLogDatabaseConnector(self.rm).getConnection()
		self.con.kayooLog.authenticate(self.rm["user_log_database"], self.rm["psswd_log_database"], mechanism='SCRAM-SHA-1')
		self.db = self.con[self.rm["name_log_database"]]
		return self.db
