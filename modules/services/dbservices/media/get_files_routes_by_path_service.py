# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import os

class GetFilesRoutesByPathService(IService):
    def __init__(self, core, parameters):
        super(GetFilesRoutesByPathService, self).__init__(core, parameters)

    def run(self):
        try:
            path = self.parameters.get("path", 'unknown/')
            realPath = self.core.GetMediaResources()["media_folder"] + path
            if not os.path.exists(realPath):
                return
            files = os.listdir(realPath)
            return [{'url':self.core.InternalOperation("getMediaRoute", {"service": "getFileByPath",
                                                                    "attribs": {"path": path,
                                                                            "filename": file}}),'name':file[:file.rfind(".")],
                                                                            'extension':file[file.rfind(".") +1:]}
                                                                                for file in files if len(files) > 0]
        except Exception, ex:
            ##No se ha encontrado la ruta hacia ese directorio
            print "Exception now!"
            print ex.message
