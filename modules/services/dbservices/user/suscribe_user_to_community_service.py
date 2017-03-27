# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime

class SuscribeUser2Community (IService):
	def __init__(self, core, parameters):
		super(SuscribeUser2Community, self).__init__(core, parameters)

	def run(self):
		try:
			_user_id = self.parameters.get("user_id",None)
			if not _user_id:
				raise Exception("Suscribe User to Community: Empty user_id not allowed.")

			user = self.core.InternalOperation("getByIdUser", {"_id":_user_id})
			_community_id = self.parameters.get("community_id", "")
			user_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _user_id})
			community_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _community_id})

			user["communities_subscribed"] = user.get("communities_subscribed", []) + [community_ObjectId]
			result = self.core.InternalOperation("updateUser", {
															"_id": user_ObjectId,
															"new_values": {
																			"communities_subscribed"	:	user["communities_subscribed"],
																			"date_modified"			:	datetime.now()
																		  }
															}
											 )
		except Exception, ex:
			print "Suscribe User to Community has failed, " + ex.message
		return result
