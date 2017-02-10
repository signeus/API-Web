# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64

class GetByIdUserService (IService):
	def __init__(self, core, parameters):
		super(GetByIdUserService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		result = DBService(self.core).getById("Users", str(self.parameters['_id']))
		##Loading the image
		avatarFile = open("/home/kevin/Pictures/avatares/" + self.parameters["_id"] + ".png","rb")
		#decodeFile = base64.b64decode(avatarFile.read())
		encodeFile = base64.b64encode(avatarFile.read())
		avatarFile.close()
		##End loading the image
		result["avatar"] = encodeFile
		return result
