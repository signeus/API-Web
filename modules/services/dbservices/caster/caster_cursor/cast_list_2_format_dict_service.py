# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastList2FormatDictService (IService):
    def __init__(self, core, parameters):
        super(CastList2FormatDictService, self).__init__(core, parameters)

    def run(self):
        lis = self.parameters.get("lis", None)
        dictionary = [c for c in lis]
        newDictionary = {}
        for elem in dictionary:
            newObject = {}
            newKey = str(elem.pop('_id'))
            newObject[newKey] = elem
            newDictionary = dict(newDictionary, **newObject)
        return newDictionary