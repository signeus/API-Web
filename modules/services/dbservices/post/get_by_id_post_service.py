# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetByIdPostService (IService):
	def __init__(self, core, parameters):
		super(GetByIdPostService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		return DBService().getById("Posts", self.parameters['_id'])
