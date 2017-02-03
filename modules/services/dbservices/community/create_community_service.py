# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64

class CreateCommunityService (IService):
	def __init__(self, core, parameters):
		super(CreateCommunityService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		image = self.parameters.get("banner", None)
		self.parameters.pop("banner", None)
		#del self.parameters["banner"]
		record =  DBService().insertIn2Collection("Communities", self.parameters)
		result = self.core.UserOperation("suscribeUser2Community", {"id_user":record["id_creator"],"id_community":record["_id"]})
		if image:
			##Saving the image
			path = "/home/kevin/Pictures/banners/" + str(record["_id"]) + ".png"
			avatarFile = open(path, "wb")
			decodeFile = base64.b64decode(image)
			##encodeFile = base64.b64encode(self.parameters["avatar"])
			avatarFile.write(decodeFile)
			avatarFile.close()
			##End Saving the image
		return record

