# -*- coding: utf-8 -*-
from datetime import datetime

class CasterDatetime:
    # TODO Optimize the class
    def castDictionaryDateObject2DateTimeStamp(self, lis):
        for elem in lis:
            for key,value in elem.iteritems():
                if type(value).__name__ == "datetime":
                    elem[key] = value.strftime("%s")
        return lis

    def castDateObject2DateTimeStamp(self, dateObject):
        return int(dateObject.strftime("%s"))
