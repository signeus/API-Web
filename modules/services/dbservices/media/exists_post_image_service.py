# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class ExistsPostImageService(IService):
    def __init__(self, core, parameters):
        super(ExistsPostImageService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", None)
        if not _id:
            raise Exception("Empty ID not allowed.")

        path = "posts/"
        filename = _id + ".png"

        return self.core.InternalOperation("existsFile", {"path":path, "filename":filename})