# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SaveFilesService(IService):
    def __init__(self, core, parameters):
        super(SaveFilesService, self).__init__(core, parameters)

    def run(self):
        files = self.parameters.get("files", [])
        path = self.parameters.get("path", '')

        print type(files)

        return [self.core.InternalOperation("saveFile", {'path': path, 'data': file["data"], 'filename': file["name"] + "." + file["extension"]}) for file in files]