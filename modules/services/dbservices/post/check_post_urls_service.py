# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CheckPostUrlsService(IService):
    def __init__(self, core, parameters):
        super(CheckPostUrlsService, self).__init__(core, parameters)

    def run(self):
        #url
        image = self.parameters.get('image',{})
        audio = self.parameters.get('audio',{})
        video = self.parameters.get('video',{})
        files = self.parameters.get('files',{})

        resultDict = {}

        urlImage = self.core.InternalOperation("validateUrl", {'url': image.get("url",None)})
        urlVideo = self.core.InternalOperation("validateUrl", {'url': video.get("url",None)})
        urlAudio = self.core.InternalOperation("validateUrl", {'url': audio.get("url",None)})

        ##TODO Test with this
        # import urllib2
        # import os
        # remotefile = urllib2.urlopen(url)
        # try:
        #     filename = remotefile.info()['Content-Disposition']
        # except KeyError:
        # filename = os.path.basename(urllib2.urlparse.urlsplit(url).path)
        ##

        filesList = [self.core.InternalOperation("validateUrl", {'url':file.get("url",None)})
                        for file in files if file.get("url",None)]
        fileAttachment = [file for file in files if file.get("data", None)]

        if urlImage and not "":
            resultDict["image"] = urlImage
        if urlVideo and not "":
            resultDict["video"] = urlVideo
        if urlAudio and not "":
            resultDict["audio"] = urlAudio
        if filesList and len(filesList) > 0:
            resultDict["files"] = filesList

        if fileAttachment and len(fileAttachment) > 0:
            resultDict["filesAttachment"] = fileAttachment

        return resultDict