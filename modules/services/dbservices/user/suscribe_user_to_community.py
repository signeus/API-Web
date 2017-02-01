# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class SuscribeUser2Community (IService):
	def __init__(self, core, parameters):
		super(SuscribeUser2Community, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters

	def run(self):
		return "suscribe"
