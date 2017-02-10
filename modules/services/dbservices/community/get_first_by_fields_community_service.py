# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetFirstByFieldsCommunityService (IService):
	def __init__(self, core, parameters):
		super(GetFirstByFieldsCommunityService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		#TODO: Filters
		return DBService(self.core).getFirstByFields("Communities", self.parameters['fields'], {})
