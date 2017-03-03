# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SaveAvatarService(IService):
    def __init__(self, core, parameters):
        super(SaveAvatarService, self).__init__(core, parameters)

    def run(self):
        path = "avatars/"
        _id = self.parameters.get("id", "")
        data = self.parameters.get("data", "")
        result = self.core.InternalOperation("saveImage",{"path":path,"file":_id, "data":data})
        if result != 0:
            raise Exception("Saving image avatar failed")
        _hex_Id = self.core.InternalOperation("castObjectId2Hex", {"id": _id})
        result = self.core.InternalOperation("getMediaRoute", {"service":"getAvatarById", "attribs":{"id": _hex_Id}})
        return result




