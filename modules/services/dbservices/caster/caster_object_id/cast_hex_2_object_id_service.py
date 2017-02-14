# -*- coding: utf-8 -*-
from bson import ObjectId
from services.interfaces.i_service import IService

class CastHex2ObjectIdService (IService):
    def __init__(self, core, parameters):
        super(CastHex2ObjectIdService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        hexId = self.parameters.get("id", None)
        if hexId and (isinstance(hexId, str) or isinstance(hexId, unicode)):
            return ObjectId(str(hexId))
        return hexId

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
