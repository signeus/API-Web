# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class castDictObjectsId2DictHexIdService (IService):
    def __init__(self, core, parameters):
        super(castDictObjectsId2DictHexIdService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        dictionary = self.parameters.get("dictionary", None)
        for key,value in dictionary.iteritems():
            if type(value).__name__ == "ObjectId":
                dictionary[key] = str(value)
        return dictionary

