# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from datetime import datetime

class SuscribeUser2Community (IService):
	def __init__(self, core, parameters):
		super(SuscribeUser2Community, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters

	def run(self):
		try:
			user = self.core.UserOperation("getByIdUser", {"_id":self.parameters["id_user"]})
			user["communities_suscribed"] = user.get("communities_suscribed", []) + [self.parameters["id_community"]]
			result = self.core.UserOperation("updateUser", {
															"_id": str(self.parameters["id_user"]),
															"new_values": {
																			"communities_suscribed"	:	user["communities_suscribed"],
																			"date_modified"			:	datetime.now()
																		  }
															}
											 )
		except Exception, ex:
			print "Suscribe User to Community has failed, " + ex.message
		return result
