# -*- coding: utf-8 -*-
from interfaces.i_service import IService

class CreateUserService (IService):
	def __init__(self, core, parameters):
		super(CreateUserService, self).__init__(core, parameters)
		
	def run(self):
		return "Esta funcionando"
