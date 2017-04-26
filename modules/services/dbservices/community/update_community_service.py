# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class UpdateCommunityService (IService):
	def __init__(self, core, parameters):
		super(UpdateCommunityService, self).__init__(core, parameters)
		
	def run(self):
		return DBService(self.core).updateIn2Collection('Communities', self.parameters['_id'], self.parameters['new_values'])
