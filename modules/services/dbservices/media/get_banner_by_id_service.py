# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import io
from PIL import Image
import time

class GetBannerByIdService(IService):
    def __init__(self, core, parameters):
        super(GetBannerByIdService, self).__init__(core, parameters)

    def run(self):
        try:
            _id = self.parameters.get("_id", '0')
            response = self.parameters.get("response", None)
            if not _id == '0':
                name = _id + self.core.InternalOperation("getFileTypeService",{"type":"images","ext":"png"})
            try:
                myfile = io.BytesIO(open("/home/www/media/banners/" + name, "rb").read())
            except Exception, ex:
                name = "default.png"
                myfile = io.BytesIO(open("/home/www/media/banners/" + name, "rb").read())
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
