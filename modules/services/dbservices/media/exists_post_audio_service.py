# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class ExistsPostAudioService(IService):
    def __init__(self, core, parameters):
        super(ExistsPostAudioService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", None)
        if not _id:
            raise Exception("Empty ID not allowed.")

        path = "posts/"
        filename = _id + ".mp3"

        return self.core.InternalOperation("existsFile", {"path":path, "filename":filename})