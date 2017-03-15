# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime
import base64
from PIL import Image
import magic
from io import BytesIO

class SaveImageService(IService):
    def __init__(self, core, parameters):
        super(SaveImageService, self).__init__(core, parameters)

    def run(self):
        data = self.parameters.get("data", '')
        timeNow = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        path = self.parameters.get("path", 'unknown/')
        file = self.parameters.get("filename", timeNow)
        if file == "":
            file = timeNow
        path = self.core.GetMediaResources()["media_folder"] + path
        format = data[:data.rfind(",")]
        data = data[data.find(",") + 1:]
        decodeFile = base64.b64decode(data)
        realMime = magic.Magic(mime=True).from_buffer(decodeFile)
        ext = realMime[realMime.rfind("/") + 1:]
        filename = file + "." +str(ext).lower()
        path = path + filename
        imageFile = Image.open(BytesIO(decodeFile))
        imageFile.save(path, str(imageFile.format))
        imageFile.close()
        return file
