# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class castListObjectsId2ListHexIdService (IService):
    def __init__(self, core, parameters):
        super(castListObjectsId2ListHexIdService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        lis = self.parameters.get("lis", None)
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
