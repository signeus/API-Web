# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SaveDirVideoService(IService):
    def __init__(self, core, parameters):
        super(SaveDirVideoService, self).__init__(core, parameters)

    def run(self):
        path = self.parameters.get("path", "unknown/")
        _id = self.parameters.get("id", "")
        data = self.parameters.get("data", "")
        return self.core.InternalOperation("saveVideo",{"path":path,"filename":str(_id), "data":data})

