# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastDictObjectsId2DictHexIdService (IService):
    def __init__(self, core, parameters):
        super(CastDictObjectsId2DictHexIdService, self).__init__(core, parameters)

    def run(self):
        return {key:str(value) for key,value in self.parameters.get("dictionary", {}).iteritems() if type(value).__name__ == "ObjectId"}

