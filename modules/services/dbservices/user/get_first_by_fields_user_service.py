# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetFirstByFieldsUserService (IService):
	def __init__(self, core, parameters):
		super(GetFirstByFieldsUserService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		#TODO: Filters
		return DBService().getFirstByFields("Users", self.parameters['fields'], {})
