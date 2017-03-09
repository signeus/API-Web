# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import time

class GetFileByPathService(IService):
    def __init__(self, core, parameters):
        super(GetFileByPathService, self).__init__(core, parameters)

    def run(self):
        try:
            path = self.parameters.get("path", 'unknown/')
            filename = self.parameters.get("filename", 'default.txt')
            path = self.core.GetMediaResources()["media_folder"] + path
            response = self.parameters.get("response", None)
            file = open(path + filename, "rb").read()
            response.body.write(file)
            #response.headers['Content-Type'] = "application/octet-stream"
            response.headers['Content-Type'] = "application/x-msdownload"
            response.headers['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            response.headers["Cache-Control"] = "private"
            response.headers["Expires"] = time.strftime("%a, %d-%b-%Y %T GMT",
                                                        time.gmtime(time.time() + 30 * 24 * 3600))
            response.headers["Pragma"] = "cache"
            response.headers["Content-Length"] = len(response.body.getvalue())
        except Exception, ex:
            print ex.message
