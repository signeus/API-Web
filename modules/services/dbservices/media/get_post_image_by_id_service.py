# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetPostImageByIdService(IService):
    def __init__(self, core, parameters):
        super(GetPostImageByIdService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "posts/"
        return self.core.InternalOperation("getDirImageById", self.parameters)