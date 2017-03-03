# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime
import base64
from PIL import Image

class SaveImageService(IService):
    def __init__(self, core, parameters):
        super(SaveImageService, self).__init__(core, parameters)

    def run(self):
        data = self.parameters.get("data", '')
        timeNow = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        path = self.parameters.get("path", 'unknown/')
        file = self.parameters.get("file", timeNow)
        if file == "":
            file = timeNow
        realPath = "/home/www/media/"
        path = realPath + path + file + ".png"
        decodeFile = base64.b64decode(data)
        #Old
        #imageFile = open(path, "wb")
        imageFile = Image.open(BytesIO(decodeFile))
        imageFile.write(decodeFile)
        imageFile.close()
        return 0

