# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_object_id import CasterObjectId
from casters.caster_datetime import CasterDatetime

class UpdatePostService (IService):
	def __init__(self, core, parameters):
		super(UpdatePostService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters

	def run(self):
		result = DBService(self.core).updateIn2Collection('Posts', self.parameters['_id'], self.parameters['new_values'])
		result = CasterObjectId().castDictObjectsId2DictHexId(result)
		result = CasterDatetime().castDictDateObject2DateTimeStamp(result)
		return result
