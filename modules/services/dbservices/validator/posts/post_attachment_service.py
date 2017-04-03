# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class PostAttachmentService (IService):
    def __init__(self, core, parameters):
        super(PostAttachmentService, self).__init__(core, parameters)

    def run(self):
        post = self.parameters.get("post","")
        _id = self.parameters.get("post_id","")

        if not _id:
            raise Exception("Post attachment service: Empty id is not allowed.")

        ##Image
        if self.core.InternalOperation("existsPostImage", {"id": _id}):  ##If exists...
            image = self.core.InternalOperation("getMediaRoute",
                                                {"service": "getPostImageById", "attribs": {"id": _id}})
            post["image"] = {'url': image}
        ##Video
        if self.core.InternalOperation("existsPostVideo", {"id": _id}):
            video = self.core.InternalOperation("getMediaRoute",
                                                {"service": "getPostVideoById", "attribs": {"id": _id}})
            post["video"] = {'url': video}
        ##Audio
        if self.core.InternalOperation("existsPostAudio", {"id": _id}):
            audio = self.core.InternalOperation("getMediaRoute",
                                                {"service": "getPostAudioById", "attribs": {"id": _id}})
            post["audio"] = {'url': audio}
        ##Files
        files = self.core.InternalOperation("getPostFiles", {"id": _id})
        if files:
            post["files"] = files


        return post