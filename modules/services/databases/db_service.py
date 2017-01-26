# -*- coding: utf-8 -*-
import types
from databases.mongo_database_manager import MongoDatabaseManager
from casters.caster_object_id import CasterObjectId

class DBService:
	
	def openCollection(self, collection):
		db = MongoDatabaseManager().connect2Database("warehouse")
		collection = db[collection]
		return collection

	def insertIn2Collection(self, collection, data):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		result = col.insert(data)
		return result

	def updateIn2Collection(self, _id, collection, new_values):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		value = col.find_one_and_update({"id" : caster.castHex2ObjectId(_id)},{'$set' : new_values}, return_document=ReturnDocument.AFTER)
		return value
	
	"""
		return: the count of rows affected.
	"""
	def deleteIn2Collection(self, _id, collection):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		if col.count({"_id": caster.castHex2ObjectId(_id)}) <= 0:
			return "No existe ese registro"
		result = col.delete_one({"_id": caster.castHex2ObjectId(_id)})
		return result

	def getFirstByFields(self, fields, filters, collection):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		#TODO: The filters
		values = col.find_one(fields)
		if type(values) == types.NoneType or len(values) <= 0:
			return "No hay resultados"
		result = {}
		for key,value in values.iteritems():
			result.update({str(key):str(value)})
		return result

	def getById(self, _id, collection):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		values = col.find_one({"_id" : _id})
		if type(values) == types.NoneType or len(values) <= 0:
			return "No hay resultados"
		result = {}
		for key,value in values.iteritems():
			result.update({str(key):str(value)})
		return result

	def getAllOfCollection(self, collection):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		values = col.find({})
		if type(values) == types.NoneType:
			return "No hay resultados"
		lista = [elem for elem in col.find({})]
		result = []
		for row in lista:
			rowResult = {}
			for key, value in row.iteritems():
				rowResult.update({str(key):str(value)})
			result.append(rowResult)
		return result
