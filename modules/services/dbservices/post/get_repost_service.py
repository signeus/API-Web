# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetRepostService (IService):
    def __init__(self, core, parameters):
        super(GetRepostService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", "")

        if not _id:
            raise Exception("Get Repost: Empty post id not allowed.")

        #Retrieve the Repost
        repost = self.core.InternalOperation("getPostById", {"id": _id})

        dictRepost = {}
        dictRepost["header"] = repost.get("repost", "")
        dictRepost["repost_id"] = _id

        #Find the post_id to refer
        post_id = repost.get("post_id", "")
        result = self.core.InternalOperation("getPost", {"post_id": post_id})

        result[result.keys()[0]]["count_repost"] =  self.core.InternalOperation("countCommentsByPost", {"post_id": post_id})
        result[result.keys()[0]]["repost"] = dictRepost
        return result