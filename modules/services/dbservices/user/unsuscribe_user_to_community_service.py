# -*- coding: utf-8 -*-
from casters.caster_object_id import CasterObjectId
from services.interfaces.i_service import IService
from datetime import datetime

class UnsuscribeUser2Community (IService):
	def __init__(self, core, parameters):
		super(UnsuscribeUser2Community, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters

	def run(self):
		try:
			user = self.core.UserOperation("getByIdUser", {"_id":self.parameters["id_user"]})
			id_community = self.parameters["id_community"]
			user["communities_suscribed"] = user.get("communities_suscribed", [])
			if user["communities_suscribed"] != []:
				user["communities_suscribed"].remove(CasterObjectId().castHex2ObjectId(id_community))
			result = self.core.InternalOperation("updateUser", {
															"_id": CasterObjectId().castHex2ObjectId(self.parameters["id_user"]),
															"new_values": {
																			"communities_suscribed"	:	user["communities_suscribed"],
																			"date_modified"			:	datetime.now()
																		  }
															}
											 )
		except Exception, ex:
			print "Unsuscribe User to Community has failed, " + ex.message
		return result
