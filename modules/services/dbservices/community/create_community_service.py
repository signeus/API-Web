# -*- coding: utf-8 -*-
from service.interfaces.i_service import IService
from services.databases.db_service import DBService

class CreateCommunityService (IService):
	def __init__(self, core, parameters):
		super(CreateCommunityService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		return DBService().insertIn2Collection("Communities", self.parameters)
