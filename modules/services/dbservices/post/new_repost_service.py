# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewRepostService (IService):
    def __init__(self, core, parameters):
        super(NewRepostService, self).__init__(core, parameters)

    def run(self):
        post_object_id = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters.get("post_id","")})
        self.parameters["post_id"] = post_object_id

        user_object_id = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters.get("user_id", "")})
        self.parameters["user_id"] = user_object_id

        community_object_id = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters.get("community_id", "")})
        self.parameters["community_id"] = community_object_id

        _repost_header = self.parameters.get("repost", "")
        self.parameters["repost"] = _repost_header

        result = self.core.InternalOperation("createPost", self.parameters)
        return result