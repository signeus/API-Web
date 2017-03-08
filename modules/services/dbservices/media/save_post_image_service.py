# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SavePostImageService(IService):
    def __init__(self, core, parameters):
        super(SavePostImageService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "posts/"
        result = self.core.InternalOperation("saveDirImage", self.parameters)
        if result == 1:
            raise Exception("Saving image post failed")
        return self.core.InternalOperation("getMediaRoute", {"service":"getPostImageById", "attribs": {"id": result}})
