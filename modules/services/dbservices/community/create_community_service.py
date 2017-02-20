# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64
from PIL import Image
from io import BytesIO

class CreateCommunityService (IService):
    def __init__(self, core, parameters):
        super(CreateCommunityService, self).__init__(core, parameters)

    def run(self):
        image = self.parameters.get("banner", None)
        self.parameters.pop("banner", None)
        #del self.parameters["banner"]
        try:
            record =  DBService(self.core).insertIn2Collection("Communities", self.parameters)
            result = self.core.InternalOperation("suscribeUser2Community", {"id_user":record["id_creator"],"id_community":record["_id"]})
            if image:
                ##Saving the image
                image = str(image)
                #format = image[:image.find(",")]
                image = image[image.find(",") + 1:]
                decodeFile = base64.b64decode(image)
                img = Image.open(BytesIO(decodeFile))
                img.save("/home/kevin/Pictures/banners/" + str(record["_id"]) + str(img.format).lower(), str(img.format))
                ##End Saving the image
            return result
        except Exception, ex:
            print ex
        return record

