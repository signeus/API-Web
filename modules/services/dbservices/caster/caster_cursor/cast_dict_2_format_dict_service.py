# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastDict2FormatDictService (IService):
    def __init__(self, core, parameters):
        super(CastDict2FormatDictService, self).__init__(core, parameters)

    def run(self):
        dictionary = self.parameters.get("dictionary", None)
        newKey = str(dictionary.pop('_id'))
        newDictionary = {}
        newDictionary[newKey] = dictionary
        return newDictionary
