# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class CreateUserService (IService):
	def __init__(self, core, parameters):
		super(CreateUserService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		_id = DBService().insertIn2Collection("Users", self.parameters)
		##Saving the image
		avatarFile = open("/home/kevin/Pictures/avatares/" + _id + ".png","wb")
		avatarFile.write(self.parameters["avatar"])
		avatarFile.close()
		##End Saving the image
		del self.parameters["avatar"]
		return _id
