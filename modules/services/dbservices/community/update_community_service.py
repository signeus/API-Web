# -*- coding: utf-8 -*-
from service.interfaces.i_service import IService
from services.databases.db_service import DBService

class UpdateCommunityService (IService):
	def __init__(self, core, parameters):
		super(UpdateCommunityService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		return DBService().updateIn2Collection('Communities', self.parameters['_id'], self.parameters['new_values'])
