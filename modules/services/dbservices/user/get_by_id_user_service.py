# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64

class GetByIdUserService (IService):
	def __init__(self, core, parameters):
		super(GetByIdUserService, self).__init__(core, parameters)

	def run(self):
		_hex_Id = self.core.InternalOperation("castObjectId2Hex",{"id" : self.parameters['_id']})
		result = DBService(self.core).getById("Users", _hex_Id)
		##Loading the image
		avatarFile = open("/home/www/media/avatars/" + _hex_Id + ".png","rb")
		#decodeFile = base64.b64decode(avatarFile.read())
		encodeFile = base64.b64encode(avatarFile.read())
		avatarFile.close()
		##End loading the image
		result["avatar"] = encodeFile
		return result
