# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewPostService (IService):
    def __init__(self, core, parameters):
        super(NewPostService, self).__init__(core, parameters)

    def run(self):
        _comment_id = self.parameters.get("community_id", None)
        if _comment_id:
            self.parameters["community_id"] = self.core.InternalOperation("castHex2ObjectId", {"id": _comment_id})

        video = self.parameters.pop("video", {})
        image = self.parameters.pop("image", {})
        files = self.parameters.pop("files", {})
        audio = self.parameters.pop("audio", {})

        checkedUrls = self.core.InternalOperation("checkPostUrls", {"video":video,"image":image,"files":files,"audio":audio})

        files = checkedUrls.pop("filesAttachment",None)
        self.parameters = dict(self.parameters, **checkedUrls)

        result = self.core.InternalOperation("createPost",self.parameters)

        id = result.get("_id", None)
        if not id:
            raise Exception("New post, Failed the create post.")

        for key, value in checkedUrls.iteritems():
            if key == "video":
               result['video'] = {'url':result['video'], 'external': True}
               video = None
            if key == "audio":
                result['audio'] = {'url': result['audio'], 'external': True}
                audio = None
            if key == "image":
                result['image'] = {'url': result['image'], 'external': True}
                image = None

        #TODO New service "POST Attachment"
        if files:
            filesRoutes = self.core.InternalOperation("savePostFiles", {'id': id, 'files': files})
            #dict(result.get("files",{}), **{'files':filesRoutes})
            result["files"] = filesRoutes

        if audio:
            urlAudio = self.core.InternalOperation("savePostAudio", {'id': id, 'data': audio.get("data",None)})
            if type(urlAudio) == str:
                result['audio'] = {'url': urlAudio}

        if image:
            urlImage = self.core.InternalOperation("savePostImage", {'id':id, 'data':image.get("data",None)})
            if type(urlImage) == str:
                result['image'] = {'url':urlImage}
        if video:
            urlVideo = self.core.InternalOperation("savePostVideo", {'id':id, 'data':video.get("data",None)})
            if type(urlVideo) == str:
                result['video'] = {'url':urlVideo}

        return result