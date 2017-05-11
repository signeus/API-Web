# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import io
from PIL import Image
import time

class GetDirImageByIdService(IService):
    def __init__(self, core, parameters):
        super(GetDirImageByIdService, self).__init__(core, parameters)

    def run(self):
        path = self.parameters.get("path", 'unknown/')
        path = self.core.GetMediaResources()["media_folder"] + path
        _id = self.parameters.get("id", '0')
        response = self.parameters.get("response", None)
        if _id != '0':
            name = _id + self.core.InternalOperation("getFileTypeService",{"type":"images", "ext":"png"})
            #name = _id + self.core.InternalOperation("getFileTypeService")
        try:
            myfile = io.BytesIO(open(path + name, "rb").read())
        except Exception, ex:
            name = "default.png"
            myfile = io.BytesIO(open(path + name, "rb").read())
        image = Image.open(myfile)
        image.save(response.body, image.format)
        response.headers['Content-Type'] = "image/" + image.format.lower()
        response.headers["Cache-Control"] = "public, max-age=3600, must-revalidate"
        response.headers["Expires"] = time.strftime("%a, %d-%b-%Y %T GMT",
                                                    time.gmtime(time.time() + 30 * 24 * 3600))
        response.headers["Pragma"] = "cache"
        response.headers["Content-Length"] = len(response.body.getvalue())
