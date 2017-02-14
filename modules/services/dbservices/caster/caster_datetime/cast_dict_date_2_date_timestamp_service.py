# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class castDictDate2DateTimeStamp (IService):
    def __init__(self, core, parameters):
        super(castDictDate2DateTimeStamp, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        dictionary = self.parameters.get("dictionary", None)
        for key,value in dictionary.iteritems():
            if type(value).__name__ == "datetime":
                dictionary[key] = value.strftime("%s")


    def castDateObject2DateTimeStamp(self, dateObject):
        return int(dateObject.strftime("%s"))
