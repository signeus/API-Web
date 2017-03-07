# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64

class CreateUserService (IService):
	def __init__(self, core, parameters):
		super(CreateUserService, self).__init__(core, parameters)

	def run(self):
		try:
			return DBService(self.core).insertIn2Collection("Users", self.parameters)
		except Exception, ex:
			print ex.message