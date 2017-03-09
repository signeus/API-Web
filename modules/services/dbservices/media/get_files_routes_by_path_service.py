# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import os

class GetFilesRoutesByPathService(IService):
    def __init__(self, core, parameters):
        super(GetFilesRoutesByPathService, self).__init__(core, parameters)

    def run(self):
        try:
            path = self.parameters.get("path", 'unknown/')
            path = self.core.GetMediaResources()["media_folder"] + path
            files = os.listdir(path)

            routesFiles = []
            if len(files) > 0:
                for file in files:
                    routesFiles.append(self.core.InternalOperation("getMediaRoute", {"service": "getFileByPath",
                                                                    "attribs": {"path": path,
                                                                            "filename": file}}))

            return routesFiles
        except Exception, ex:
            print ex.message
