# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SavePostAudioService(IService):
    def __init__(self, core, parameters):
        super(SavePostAudioService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "posts/"
        result = self.core.InternalOperation("saveDirAudio", self.parameters)
        if type(result) != str:
            return result

        return self.core.InternalOperation("getMediaRoute", {"service":"getPostAudioById", "attribs": {"id": result}})
