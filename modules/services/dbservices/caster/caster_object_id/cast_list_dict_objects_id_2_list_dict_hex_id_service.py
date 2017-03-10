# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastListDictObjectsId2ListDictHexIdService (IService):
    def __init__(self, core, parameters):
        super(CastListDictObjectsId2ListDictHexIdService, self).__init__(core, parameters)

    def run(self):
        return [{key: str(value) for key, value in elem.iteritems() if type(value).__name__ == "ObjectId"} for elem in self.parameters.get("lis", [])]