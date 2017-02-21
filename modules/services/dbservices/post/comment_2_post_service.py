# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class Comment2PostService (IService):
	def __init__(self, core, parameters):
		super(Comment2PostService, self).__init__(core, parameters)
		
	def run(self):
		try:
			result = self.core.InternalOperation("createPost", self.parameters)
			return result
		except Exception, ex:
			print ex.message
