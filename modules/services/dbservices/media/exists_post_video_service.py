# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class ExistsPostVideoService(IService):
    def __init__(self, core, parameters):
        super(ExistsPostVideoService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", None)
        if not _id:
            raise Exception("Empty ID not allowed.")

        path = "posts/"
        filename = _id + ".mp4"

        return self.core.InternalOperation("existsFile", {"path":path, "filename":filename})