# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from datetime import datetime

class CreatePostService (IService):
	def __init__(self, core, parameters):
		super(CreatePostService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		try:
			result = DBService().insertIn2Collection("Posts", self.parameters)
			result["date_created"] = int(result["date_created"].strftime("%s"))
			result["date_modified"] = int(result["date_modified"].strftime("%s"))
			result["action"] = "ok"
			result["_id"] = str(result["_id"])
		except Exception, ex:
			print ex.message
		return result
