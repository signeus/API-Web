# -*- coding: utf-8 -*-
import types
from datetime import datetime
from databases.mongo_database_manager import MongoDatabaseManager
from casters.caster_object_id import CasterObjectId
from casters.caster_datetime import CasterDatetime
from pymongo.collection import ReturnDocument

class DBService:
    def __init__(self, core):
        self.core = core

    def insertDateCreated(self, data):
        try:
            data["date_created"] = datetime.utcnow()#.strftime('%Y-%m-%d %H:%M:%S')
            data["date_modified"] = datetime.utcnow()#.strftime('%Y-%m-%d %H:%M:%S')
            return data
        except Exception, e:
            return "Has been appears a issue with the Json 'Date_Created'\n Exception: " + e.message

    def insertDateModified(self, data):
        try:
            data["date_modified"] = datetime.utcnow()#.strftime('%Y-%m-%d %H:%M:%S')
            return data
        except Exception, e:
            return "Has been appears a issue with the Json 'Date_Modified'\n Exception: " + e.message
	
    def openCollection(self, collection):
        db = MongoDatabaseManager(self.core.GetDatabaseResources()).connect2Database()
        collection = db[collection]
        return collection

    def insertIn2Collection(self, collection, data):
        col = self.openCollection(collection)
        data_completed = self.insertDateCreated(data)
        result = col.insert(data_completed)
        if len(str(result)) <= 0:
            raise Exception("Error inserting")
        data_completed["_id"] = str(result)
        data_completed["date_created"] = CasterDatetime().castDateObject2DateTimeStamp(data_completed["date_created"])
        data_completed["date_modified"] = CasterDatetime().castDateObject2DateTimeStamp(data_completed["date_modified"])
        return data_completed

    def updateIn2Collection(self, collection, _id, new_values):
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _id})
        col = self.openCollection(collection)
        data_completed = self.insertDateModified(new_values)
        value = col.find_one_and_update(
										{"_id"   : _ObjectId},
										{'$set'  : data_completed},
										return_document=ReturnDocument.AFTER
									   )
        return value

    def updateMultiByFieldWithDelete(self, collection, field, id):
        col = self.openCollection(collection)
        result = col.update({ field : { "$in" : [CasterObjectId().castHex2ObjectId(id)]} },{"$pull" : { field : CasterObjectId().castHex2ObjectId(id)}}, multi=True)
        return result

    """
        return: the count of rows affected.
    """
    def deleteIn2Collection(self, collection, _id):
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _id})
        col = self.openCollection(collection)
        if col.count({"_id": _ObjectId}) <= 0:
            return "Not founded that id"
        result = col.delete_one({"_id": _ObjectId})
        return result.deleted_count

    def getById(self, collection, _id):
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _id})
        col = self.openCollection(collection)
        values = col.find_one({"_id": _ObjectId})
        if type(values) == types.NoneType or len(values) <= 0:
            return "Not founded results"
        result = {}
        values["date_created"] = int(values["date_created"].strftime("%s"))
        values["date_modified"] = int(values["date_modified"].strftime("%s"))
        for key, value in values.iteritems():
            result.update({str(key): value})
        return result

    def getFirstByFields(self, collection, fields, filters):
        col = self.openCollection(collection)
        #TODO: The filters
        values = col.find_one(fields)
        if type(values) == types.NoneType or len(values) <= 0:
            return "Not founded results"
        result = {}
        for key,value in values.iteritems():
            result.update({str(key):value})
        return result

    def getAll(self, collection):
        col = self.openCollection(collection)
        values = col.find({}).sort("date_modified", -1) #ASCENDING
        if type(values) == types.NoneType:
            return "Not founded results"
        result = [c for c in values]
        return result

    def getAllByFilter(self, collection, query, opt_filter={}):
        col = self.openCollection(collection)
        values = col.find(query, opt_filter).sort("date_modified", -1) #ASCENDING
        return [c for c in values]

    def updateFieldInside(self, collection, _id, new_values):
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _id})
        col = self.openCollection(collection)
        #data_completed = self.insertDateModified(new_values)
        print _ObjectId
        # value = col.update({ '_id': 5 },
        #                        {
        #                          '$push': {
        #                            'quizzes': {'scores': 90}
        #                          }
        #                        }
        #                     )

        # db.collection.update(
        #     {"_id": ID, "playlists._id": "58"},
        #     {"$push":
        #         {"playlists.$.musics":
        #             {
        #                 "name": "test name",
        #                 "duration": "4.00"
        #             }
        #         }
        #     }
        # )
        print type(_ObjectId)
        value = col.update({'_id': '5'},
                           {
                               '$push': {
                                   'survey.$.answers': ['5891cced481f3416aa786783']
                               }
                           }
                           )

        # value = col.update({'_id': _ObjectId },{'$push': {'survey':
        #                                                             { 'answers':
        #                                                                 {
        #                                                                     '$each':['5891cced481f3416aa786783']
        #                                                                 }
        #                                                             }
        #                                                 }
        #                                         })
        print value
        print "he terminado"
        return value

        #
        #value = col.update({'': {'$ne':''} },{'$push': {'':{'$each':['']}}},
        #										return_document=ReturnDocument.AFTER)
        #
        #db.threads.update({'messages.read_by': {$ne: 'jim'}},{$push: {'messages.read_by': {$each: ['jim']}}})