# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetAllCommunityService (IService):
	def __init__(self, core, parameters):
		super(GetAllCommunityService, self).__init__(core, parameters)
		
	def run(self):
		return DBService(self.core).getAll("Communities")
