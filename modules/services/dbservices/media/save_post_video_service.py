# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import types

class SavePostVideoService(IService):
    def __init__(self, core, parameters):
        super(SavePostVideoService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "posts/"
        result = self.core.InternalOperation("saveDirVideo", self.parameters)
        if type(result) != str:
            return result

        return self.core.InternalOperation("getMediaRoute", {"service":"getPostVideoById", "attribs": {"id": result}})
