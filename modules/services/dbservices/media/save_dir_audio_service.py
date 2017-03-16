# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SaveDirAudioService(IService):
    def __init__(self, core, parameters):
        super(SaveDirAudioService, self).__init__(core, parameters)

    def run(self):
        path = self.parameters.get("path", "unknown/")
        _id = self.parameters.get("id", "")
        data = self.parameters.get("data", "")
        return self.core.InternalOperation("saveAudio",{"path":path,"filename":str(_id), "data":data})

