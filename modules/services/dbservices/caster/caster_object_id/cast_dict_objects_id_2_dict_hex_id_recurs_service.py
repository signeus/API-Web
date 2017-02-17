# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastDictObjectsId2DictHexIdRecursService (IService):
    def __init__(self, core, parameters):
        super(CastDictObjectsId2DictHexIdRecursService, self).__init__(core, parameters)

    def run(self):
        iter = self.parameters.get("iter", None)
        if type(iter).__name__ == "list":
            iter = self.listFound(self.parameters.get("iter", []))
        if type(iter).__name__ == "dict":
            iter = self.dictFound(self.parameters.get("iter", {}))
        return iter

    def dictFound(self, dict):
        for key, value in dict.iteritems():
            if type(value).__name__ == "dict":
                dict[key] = self.dictFound(value)
            if type(value).__name__ == "list":
                dict[key] = self.listFound(value)
            if type(value).__name__ == "ObjectId":
                dict[key] = str(value)
            if type(value).__name__ == "datetime":
                dict[key] = value.strftime("%s")
        return dict

    def listFound(self, lis):
        for elem in lis :
            if type(elem).__name__ == "dict":
                self.dictFound(elem)
            if type(elem).__name__ == "list":
                self.listFound(elem)
            if type(elem).__name__ == "ObjectId":
                lis[lis.index(elem)] = str(elem)
            if type(elem).__name__ == "datetime":
                lis[lis.index(elem)] = elem.strftime("%s")
        return lis
