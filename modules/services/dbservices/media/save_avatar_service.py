# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SaveAvatarService(IService):
    def __init__(self, core, parameters):
        super(SaveAvatarService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "avatars/"
        result = self.core.InternalOperation("saveDirImage", self.parameters)
        if result == 1:
            raise Exception("Saving image avatar failed")
        return self.core.InternalOperation("getMediaRoute", {"service":"getAvatarById", "attribs":{"id": result}})


