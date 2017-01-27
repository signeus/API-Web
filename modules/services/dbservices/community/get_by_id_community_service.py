# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.databases.db_service import DBService

class GetByIdCommunityService (IService):
	def __init__(self, core, parameters):
		super(GetByIdCommunityService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		return DBService().getById("Communities", self.parameters['_id'])
