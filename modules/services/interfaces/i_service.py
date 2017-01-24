# -*- coding: utf-8 -*-

class IService (object):
	def __init__(self, core, parameters):
		self.core = core
		self.parameters = parameters
		
	def run(self):
		pass
