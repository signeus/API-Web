# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import os

class SaveFileService(IService):
    def __init__(self, core, parameters):
        super(SaveFileService, self).__init__(core, parameters)

    def run(self):
        try:
            data = self.parameters.get("data", '')
            relativePath = self.parameters.get("path", 'unknown/')
            filename = self.parameters.get("filename", "")
            if filename == "":
                from datetime import datetime
                timeNow = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                filename = timeNow
            path = self.core.GetMediaResources()["media_folder"] + relativePath

            if not os.path.exists(path):
                os.makedirs(path)
                print "Created directory in "+ path

            path = path + filename
            file = open(path, 'wb')
            file.write(str(data))
            file.close()
            return self.core.InternalOperation("getMediaRoute", {"service": "getFileByPath",
                                                                 "attribs": {"path": relativePath,
                                                                             "filename": filename}})
        except Exception, ex:
            print "Failed saving file."
            return 1

