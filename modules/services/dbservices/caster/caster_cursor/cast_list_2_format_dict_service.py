# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class castList2FormatDictService (IService):
    def __init__(self, core, parameters):
        super(castList2FormatDictService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

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

class CasterCursor:
    # TODO Optimize the class
    def castList2FormatDictionary(self, list):
        dictionary = [c for c in list]
        newDictionary = {}
        for elem in dictionary:
            newObject = {}
            newKey = str(elem.pop('_id'))
            newObject[newKey] = elem
            newDictionary = dict(newDictionary, **newObject)
        return newDictionary

    def castDictionary2FormatDictionary(self, dictionary):
        newDictionary = {}
        for k, elem in dictionary.iterItems():
            newObject = {}
            newKey = str(elem.pop('_id'))
            newObject[newKey] = elem
            newDictionary = dict(newDictionary, **newObject)
        return newDictionary