# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewPostService (IService):
    def __init__(self, core, parameters):
        super(NewPostService, self).__init__(core, parameters)

    def run(self):
        image = self.parameters.get("image", None)
        self.parameters.pop("image", None)
        result = self.core.InternalOperation("createPost",self.parameters)
        if image:
            id = self.result.get("_id", None)
            if not id:
                raise Exception("New post, Not exists the ID to generate the image.")
            urlImage = self.core.InternalOperation("savePostImage", {'id':id, 'data':image})
            result['image'] = urlImage

        return result