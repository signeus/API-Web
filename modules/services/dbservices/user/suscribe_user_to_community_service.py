# -*- coding: utf-8 -*-
from casters.caster_object_id import CasterObjectId
from services.interfaces.i_service import IService
from datetime import datetime

class SuscribeUser2Community (IService):
	def __init__(self, core, parameters):
		super(SuscribeUser2Community, self).__init__(core, parameters)

	def run(self):
		try:
			user = self.core.InternalOperation("getByIdUser", {"_id":self.parameters["id_user"]})
			user["communities_subscribed"] = user.get("communities_subscribed", []) + [CasterObjectId().castHex2ObjectId(self.parameters["id_community"])]
			result = self.core.InternalOperation("updateUser", {
															"_id": CasterObjectId().castHex2ObjectId(self.parameters["id_user"]),
															"new_values": {
																			"communities_subscribed"	:	user["communities_subscribed"],
																			"date_modified"			:	datetime.now()
																		  }
															}
											 )
		except Exception, ex:
			print "Suscribe User to Community has failed, " + ex.message
		return result
