# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class CreatePostService (IService):
	def __init__(self, core, parameters):
		super(CreatePostService, self).__init__(core, parameters)
		
	def run(self):
		try:
			return DBService(self.core).insertIn2Collection("Posts", self.parameters)
		except Exception, ex:
			print ex.message
