# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetPostVideoByIdService(IService):
    def __init__(self, core, parameters):
        super(GetPostVideoByIdService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "posts/"
        return self.core.InternalOperation("getDirVideoById", self.parameters)