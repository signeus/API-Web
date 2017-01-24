# -*- coding: utf-8 -*-
from services.service_factory import ServiceFactory

class Core:
	def UserOperation(self, serviceName, parameters):
		return self.FactoryOperation(serviceName, parameters)
		
	def CommunityOperation(self, serviceName, parameters):
		return self.FactoryOperation(serviceName, parameters)

	def FactoryOperation(self, serviceName, parameters):
		return ServiceFactory(serviceName, self, parameters).run()
