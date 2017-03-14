# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import time
import magic

class GetDirVideoByIdService(IService):
    def __init__(self, core, parameters):
        super(GetDirVideoByIdService, self).__init__(core, parameters)

    def run(self):
        path = self.parameters.get("path", 'unknown/')
        path = self.core.GetMediaResources()["media_folder"] + path
        _id = self.parameters.get("id", '0')
        response = self.parameters.get("response", None)
        if _id != '0':
            name = _id + self.core.InternalOperation("getFileTypeService",{"type":"video","ext":"mp4"})

        mime = "video/mp4" #Default MIME
        try:
            myfile = open(path + name, "rb").read()
            mime = magic.Magic(mime=True, uncompress=True).from_buffer(myfile)
        except Exception, ex:
            name = "default.mp4"
            myfile = open(path + name, "rb").read()

        response.body.write(myfile)
        response.headers['Content-Type'] = mime
        #response.headers['Content-Type'] = "application/octet-stream"
        response.headers["Cache-Control"] = "public, max-age=3600, must-revalidate"
        response.headers["Expires"] = time.strftime("%a, %d-%b-%Y %T GMT",
                                                    time.gmtime(time.time() + 30 * 24 * 3600))
        response.headers["Pragma"] = "cache"
        response.headers["Content-Length"] = len(response.body.getvalue())
