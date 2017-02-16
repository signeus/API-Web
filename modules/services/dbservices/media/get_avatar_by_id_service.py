# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import io
from PIL import Image
import time

class GetAvatarByIdService(IService):
    def __init__(self, core, parameters):
        super(GetAvatarByIdService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        try:
            _id = self.parameters.get("_id", '0')
            response = self.parameters.get("response", None)
            name = _id + self.core.InternalOperation("getFileTypeService",{"type":"images","ext":"png"})
            #myfile = io.BytesIO(open("/home/kevin/Pictures/avatares/" + name, "rb", buffering=0).read())
            myfile = io.BytesIO(open("/home/kevin/Pictures/avatares/" + name, "rb").read())
            image = Image.open(myfile)
            image.save(response.body, image.format)
            response.headers['Content-Type'] = "image/" + image.format.lower()
            response.headers["Cache-Control"] = "private"
            response.headers["Expires"] = time.strftime("%a, %d-%b-%Y %T GMT",
                                                        time.gmtime(time.time() + 30 * 24 * 3600))
            response.headers["Pragma"] = "cache"
            response.headers["Content-Length"] = len(response.body.getvalue())
        except Exception, ex:
            print ex.message
