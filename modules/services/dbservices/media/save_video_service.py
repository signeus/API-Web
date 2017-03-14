# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime
import base64
import magic

class SaveVideoService(IService):
    def __init__(self, core, parameters):
        super(SaveVideoService, self).__init__(core, parameters)

    def run(self):
        data = self.parameters.get("data", '')
        timeNow = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        path = self.parameters.get("path", 'unknown/')
        file = self.parameters.get("filename", timeNow)
        if file == "":
            file = timeNow
        path = self.core.GetMediaResources()["media_folder"] + path
        format = data[:data.rfind(",")]
        ext = format[format.rfind("/") + 1:]
        data = data[data.find(",") + 1:]
        decodeFile = base64.b64decode(data)
        filename = file + "." +str(ext).lower()
        path = path + filename
        realMime = magic.Magic(mime=True).from_buffer(decodeFile)
        if realMime != format:
            raise Exception("This video does not match uploaded format")

        videoFile = open(path, 'wb')
        videoFile.write(decodeFile)
        videoFile.close()
        return file

