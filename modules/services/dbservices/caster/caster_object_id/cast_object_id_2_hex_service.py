# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastObjectId2HexService (IService):
    def __init__(self, core, parameters):
        super(CastObjectId2HexService, self).__init__(core, parameters)

    def run(self):
        hexId = self.parameters.get("id", None)
        if hexId:
            return str(hexId)
        return hexId