# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime
import base64
from PIL import Image
from io import BytesIO

class SaveImageService(IService):
    def __init__(self, core, parameters):
        super(SaveImageService, self).__init__(core, parameters)

    def run(self):
        try:
            data = self.parameters.get("data", '')
            timeNow = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            path = self.parameters.get("path", 'unknown/')
            file = self.parameters.get("filename", timeNow)
            if file == "":
                file = timeNow
            path = "/home/www/media/" + path
            data = data[data.find(",") + 1:]
            decodeFile = base64.b64decode(data)
            imageFile = Image.open(BytesIO(decodeFile))
            path = path + file + "." +str(imageFile.format).lower()
            imageFile.save(path, str(imageFile.format))
            imageFile.close()
            return file
        except Exception, ex:
            return 1

