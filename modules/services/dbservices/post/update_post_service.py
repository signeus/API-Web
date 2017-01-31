# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class UpdatePostService (IService):
	def __init__(self, core, parameters):
		super(UpdatePostService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters

	def run(self):
		return DBService().updateIn2Collection('Posts', self.parameters['_id'], self.parameters['new_values'])
