# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetPostByIdService (IService):
	def __init__(self, core, parameters):
		super(GetPostByIdService, self).__init__(core, parameters)
		
	def run(self):
		return DBService(self.core).getById("Posts", self.parameters['id'])
