# -*- coding: utf-8 -*-
import bson
from bson import ObjectId
import json

class CasterObjectId:
    #TODO Optimize the class
    def castHex2ObjectId(self, _id):
        _id_str = str(_id)
        _id_object = ObjectId(_id_str)
        return _id_object

    def castObjectId2Hex(self, object_id):
        _id_str = str(object_id)
        return _id_str

    def castListObjectsId2DictionaryHexId(self, lis):
        for elem in lis:
            for key,value in elem.iteritems():
                if type(value).__name__ == "ObjectId":
                    elem[key] = str(value)
        return lis

    def castDictObjectsId2DictHexId(self, dictionary):
        for key,value in dictionary.iteritems():
            if type(value).__name__ == "ObjectId":
                dictionary[key] = str(value)
        return dictionary

    def castDictHex2DictObjectid(self,dictionary):
        for key, value in dictionary.iteritems():
            if "_id" in key:
                dictionary[key] = ObjectId(value)
        return dictionary

