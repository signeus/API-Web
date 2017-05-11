# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastListObjectsId2ListHexIdService (IService):
    def __init__(self, core, parameters):
        super(CastListObjectsId2ListHexIdService, self).__init__(core, parameters)

    def run(self):
        lis = [str(elem) for elem in self.parameters.get("lis", []) if type(elem).__name__ == "ObjectId"]
        return lis