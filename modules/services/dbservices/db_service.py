# -*- coding: utf-8 -*-
import types
import json
from datetime import datetime
from databases.mongo_database_manager import MongoDatabaseManager
from casters.caster_object_id import CasterObjectId
from pymongo.collection import ReturnDocument

class DBService:

    def insertDateCreated(self, data):
        try:
            data["date_created"] = datetime.utcnow()#.strftime('%Y-%m-%d %H:%M:%S')
            data["date_modified"] = datetime.utcnow()#.strftime('%Y-%m-%d %H:%M:%S')
            return data
        except Exception, e:
            return "Has been appears a issue with the Json 'Date_Created'\n Exception: " + e.message

    def insertDateModified(self, data):
        try:
            data["date_modified"] = datetime.now()#.strftime('%Y-%m-%d %H:%M:%S')
            return data
        except Exception, e:
            return "Has been appears a issue with the Json 'Date_Modified'\n Exception: " + e.message
	
    def openCollection(self, collection):
        db = MongoDatabaseManager().connect2Database("warehouse")
        collection = db[collection]
        return collection

    def insertIn2Collection(self, collection, data):
        db = MongoDatabaseManager().connect2Database("warehouse")
        col = db[collection]
        data_completed = self.insertDateCreated(data)
        result = col.insert(data_completed)
        if len(str(result)) <= 0:
            raise Exception("Error inserting")
        return data_completed

    def updateIn2Collection(self, collection, _id, new_values):
        db = MongoDatabaseManager().connect2Database("warehouse")
        col = db[collection]
        data_completed = self.insertDateModified(new_values)
        value = col.find_one_and_update(
										{"_id"   : CasterObjectId().castHex2ObjectId(_id)},
										{'$set'  : new_values},
										return_document=ReturnDocument.AFTER
									   )
        return value

    """
        return: the count of rows affected.
    """
    def deleteIn2Collection(self, collection, _id):
        db = MongoDatabaseManager().connect2Database("warehouse")
        col = db[collection]
        if col.count({"_id": CasterObjectId().castHex2ObjectId(_id)}) <= 0:
            return "Not founded that id"
        result = col.delete_one({"_id": CasterObjectId().castHex2ObjectId(_id)})
        return result.deleted_count

	def getFirstByFields(self, collection, fields, filters):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		#TODO: The filters
		values = col.find_one(fields)
		if type(values) == types.NoneType or len(values) <= 0:
			return "Not founded results"
		result = {}
		for key,value in values.iteritems():
			result.update({str(key):str(value)})
		return result

	def getById(self, collection, _id):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		values = col.find_one({"_id" : CasterObjectId().castHex2ObjectId(_id)})
		if type(values) == types.NoneType or len(values) <= 0:
			return "Not founded results"
		result = {}
		for key,value in values.iteritems():
			result.update({str(key):str(value)})
		return result

	def getAll(self, collection):
		db = MongoDatabaseManager().connect2Database("warehouse")
		col = db[collection]
		values = col.find({})
		if type(values) == types.NoneType:
			return "Not founded results"
		lista = [elem for elem in col.find({})]
		result = []
		for row in lista:
			rowResult = {}
			for key, value in row.iteritems():
				rowResult.update({str(key):str(value)})
			result.append(rowResult)
		return result
