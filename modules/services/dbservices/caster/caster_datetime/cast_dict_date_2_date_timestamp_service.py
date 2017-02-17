# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastDictDate2DateTimeStampService (IService):
    def __init__(self, core, parameters):
        super(CastDictDate2DateTimeStampService, self).__init__(core, parameters)

    def run(self):
        dictionary = self.parameters.get("dictionary", None)
        for key,value in dictionary.iteritems():
            if type(value).__name__ == "datetime":
                dictionary[key] = value.strftime("%s")
        return dictionary