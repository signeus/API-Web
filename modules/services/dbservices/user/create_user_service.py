# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64

class CreateUserService (IService):
	def __init__(self, core, parameters):
		super(CreateUserService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		image = None
		image = self.parameters["avatar"]
		del self.parameters["avatar"]
		record = DBService().insertIn2Collection("Users", self.parameters)
		if image:
			##Saving the image
			path = "/home/kevin/Pictures/avatares/" + str(record["_id"]) + ".png"
			avatarFile = open(path,"wb")
			decodeFile = base64.b64decode(image)
			##encodeFile = base64.b64encode(self.parameters["avatar"])
			avatarFile.write(decodeFile)
			avatarFile.close()
			##End Saving the image
		return record
