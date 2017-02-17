# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class castDict2FormatDictService (IService):
    def __init__(self, core, parameters):
        super(castDict2FormatDictService, self).__init__(core, parameters)

    def run(self):
        dictionary = self.parameters.get("dictionary", None)
        newDictionary = {}
        for elem in dictionary:
            newObject = {}
            newKey = str(elem.pop('_id'))
            newObject[newKey] = elem
            newDictionary = dict(newDictionary, **newObject)
        return newDictionary
