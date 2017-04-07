# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CountCommentsByPostService (IService):
    def __init__(self, core, parameters):
        super(CountCommentsByPostService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("post_id","")
        print self.parameters
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _id})

        count = self.core.InternalOperation("countPosts", {"query": {"comment":{"$exists": True}, "post_id": _ObjectId}})

        return count