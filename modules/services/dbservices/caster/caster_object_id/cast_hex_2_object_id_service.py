# -*- coding: utf-8 -*-
from bson import ObjectId
from services.interfaces.i_service import IService

class CastHex2ObjectIdService (IService):
    def __init__(self, core, parameters):
        super(CastHex2ObjectIdService, self).__init__(core, parameters)

    def run(self):
        hexId = self.parameters.get("id", None)
        if hexId and (isinstance(hexId, str) or isinstance(hexId, unicode)):
            return ObjectId(str(hexId))
        return hexId
