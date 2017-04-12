# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class CountRepostService(IService):
    def __init__(self, core, parameters):
        super(CountRepostService, self).__init__(core, parameters)


    def run(self):
        _id = self.parameters.get("post_id", "")
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _id})

        counts = self.core.InternalOperation("countPosts",
                                            {"query": {"repost": {"$exists": True}, "post_id": _ObjectId}})
        return counts

