# -*- coding: utf-8 -*-
from bson import ObjectId

class CasterObjectId:
	def castHex2ObjectId(self, _id):
		_id_str = str(_id)
		_id_object = ObjectId(_id_str)
		return _id_object
	
	def castObjectId2Hex(self, object_id):
		_id_str = str(object_id)
		return _id_str
