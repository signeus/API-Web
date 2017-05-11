# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class UpdatePostContentService (IService):
    def __init__(self, core, parameters):
        super(UpdatePostContentService, self).__init__(core, parameters)

    def run(self):
        result = self.core.InternalOperation("updatePost", {"_id":self.parameters["id"], "new_values":{"post":str(self.parameters["post"])}})
        return result