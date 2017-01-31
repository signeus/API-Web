# -*- coding: utf-8 -*-
import json
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class CreatePostService (IService):
	def __init__(self, core, parameters):
		super(CreatePostService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		result = DBService().insertIn2Collection("Posts", self.parameters)
		result["action"] = "ok"
		return result
