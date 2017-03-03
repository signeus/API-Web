# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64

class CreateUserService (IService):
	def __init__(self, core, parameters):
		super(CreateUserService, self).__init__(core, parameters)
		
	def run(self):
		image = self.parameters.get("avatar", None)
		self.parameters.pop("avatar", None)
		self.parameters["communities_subscribed"] = self.parameters.get("communities_subscribed",[])
		self.parameters["profile"] = self.parameters.get("profile",{})
		record = DBService(self.core).insertIn2Collection("Users", self.parameters)
		if image:
			##Saving the image
			path = "/home/www/media/avatars/" + str(record["_id"]) + ".png"
			avatarFile = open(path,"wb")
			decodeFile = base64.b64decode(image)
			##encodeFile = base64.b64encode(self.parameters["avatar"])
			avatarFile.write(decodeFile)
			avatarFile.close()
			##End Saving the image
		return record
