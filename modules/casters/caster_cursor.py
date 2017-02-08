# -*- coding: utf-8 -*-

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