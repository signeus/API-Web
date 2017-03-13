# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetPostFilesService(IService):
    def __init__(self, core, parameters):
        super(GetPostFilesService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", None)
        if not _id:
            raise Exception("Empty ID not allowed.")

        path = "posts/files/" + _id + "/"
        return self.core.InternalOperation("getFilesRoutesByPath", {'path': path})
