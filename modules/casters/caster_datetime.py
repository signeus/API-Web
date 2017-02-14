# -*- coding: utf-8 -*-
from datetime import datetime

class CasterDatetime:
    # TODO Optimize the class
    def castListDateObject2DateTimeStamp(self, lis):
        for elem in lis:
            for key,value in elem.iteritems():
                if type(value).__name__ == "datetime":
                    elem[key] = value.strftime("%s")
        return lis

    def castDictDateObject2DateTimeStamp(self, dictionary):
        for key,value in dictionary.iteritems():
            if type(value).__name__ == "datetime":
                dictionary[key] = value.strftime("%s")
        return dictionary

    def castDateObject2DateTimeStamp(self, dateObject):
        return int(dateObject.strftime("%s"))
