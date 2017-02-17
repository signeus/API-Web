# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class Like2PostService (IService):
    def __init__(self, core, parameters):
        super(Like2PostService, self).__init__(core, parameters)

    def run(self):
        return self.core.InternalOperation("like2Post", self.parameters) if self.parameters["status"] else self.core.InternalOperation("unlike2Post", self.parameters)