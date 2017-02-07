# -*- coding: utf-8 -*-
import bson
from bson import ObjectId

class CasterObjectId:
    def castHex2ObjectId(self, _id):
        _id_str = str(_id)
        _id_object = ObjectId(_id_str)
        return _id_object

    def castObjectId2Hex(self, object_id):
        _id_str = str(object_id)
        return _id_str

    def castDictionaryObjectsId2DictionaryHexId(self, dictionary):
        for elem in dictionary:
            for key,value in elem.iteritems():
                if type(value).__name__ == "ObjectId":
                    elem[key] = str(value)
        return dictionary