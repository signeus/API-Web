# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64

class GetByIdUserService (IService):
    def __init__(self, core, parameters):
        super(GetByIdUserService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get('_id','')
        result = DBService(self.core).getById("Users", _id)
        _hex_Id = self.core.InternalOperation("castObjectId2Hex", {"id": _id})
        result["avatar"] = self.core.InternalOperation("getMediaRoute", {"service":"getAvatarById", "attribs":{"id": _hex_Id}})
        return result
