# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class DeleteUserService (IService):
	def __init__(self, core, parameters):
		super(DeleteUserService, self).__init__(core, parameters)
		
	def run(self):
		return DBService(self.core).deleteIn2Collection('Users', self.parameters['_id'])
