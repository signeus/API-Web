# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewPostService (IService):
    def __init__(self, core, parameters):
        super(NewPostService, self).__init__(core, parameters)

    def run(self):

        _comment_id = self.parameters.get("community_id", None)
        if _comment_id:
            self.parameters["community_id"] = self.core.InternalOperation("castHex2ObjectId", {"id": _comment_id})

        image = self.parameters.get("image", None)
        self.parameters.pop("image", None)
        video = self.parameters.get("video", None)
        self.parameters.pop("video", None)


        result = self.core.InternalOperation("createPost",self.parameters)

        id = result.get("_id", None)
        if not id:
            raise Exception("New post, Failed the create post.")

        if image:
            urlImage = self.core.InternalOperation("savePostImage", {'id':id, 'data':image})
            if type(urlImage) == str:
                result['image'] = urlImage
        if video:
            urlVideo = self.core.InternalOperation("savePostVideo", {'id':id, 'data':video})
            if type(urlVideo) == str:
                result['video'] = urlVideo

        return result