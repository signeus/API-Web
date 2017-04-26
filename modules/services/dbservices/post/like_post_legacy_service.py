# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime

class Like2PostService (IService):
    def __init__(self, core, parameters):
        super(Like2PostService, self).__init__(core, parameters)

    def run(self):
        try:
            _UserObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id_user"]})
            _PostObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id"]})
            post = self.core.InternalOperation("getByIdPost", {"_id": self.parameters["id"]})
            post["likes"] = post.get("likes", []) + [_UserObjectId]
            result = self.core.InternalOperation("updatePost", {
                                                                "_id": _PostObjectid,
                                                                "new_values": {
                                                                    "likes": post["likes"],
                                                                    "date_modified"	 :	datetime.now()
                                                                }
                                                            }
                                             )
            result["likes"] = self.core.InternalOperation("castListObjectsId2ListHexId", {"lis": result["likes"]})

            #result = self.core.InternalOperation("castDictDate2DateTimestamp", {"dictionary": result})
            #result = self.core.InternalOperation("castDictObjectsId2DictHexId", {"dictionary": result})
            return result
        except Exception, ex:
            print "Like has failed, " + ex.message
        return result