# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import json

class SavePostFilesService(IService):
    def __init__(self, core, parameters):
        super(SavePostFilesService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", None)
        files = self.parameters.get("files", None)

        if not (_id or files):
            raise Exception("Save Post Files: Id or Files not founded")

        path = "posts/files/" + str(_id) +"/"
        result = self.core.InternalOperation("saveFiles", {'path':path, 'files':files})
        return result
