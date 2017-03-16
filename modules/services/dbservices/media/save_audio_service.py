# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime
import base64
import magic
import mimetypes

class SaveAudioService(IService):
    def __init__(self, core, parameters):
        super(SaveAudioService, self).__init__(core, parameters)

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
        ext = mimetypes.guess_extension(realMime)
        #realMime[realMime.rfind("/") + 1:]
        filename = file + str(ext).lower()
        path = path + filename
        audioFile = open(path, 'wb')
        audioFile.write(decodeFile)
        audioFile.close()
        return file

