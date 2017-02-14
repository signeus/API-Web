# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastHObjectId2HexService (IService):
    def __init__(self, core, parameters):
        super(CastHObjectId2HexService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        hexId = self.parameters.get("id", None)
        if hexId:
            return str(hexId)
        return hexId