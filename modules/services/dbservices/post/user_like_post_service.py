# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime

class UserLike2PostService (IService):
    def __init__(self, core, parameters):
        super(UserLike2PostService, self).__init__(core, parameters)

    def run(self):
        try:
            _UserObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["user_id"]})
            _PostObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id"]})
            post = self.core.InternalOperation("getByIdPost", {"_id": self.parameters["id"]})
            if _UserObjectId in post.get("likes", []):
                raise Exception('This user already liked the post')

            post["likes"] = post.get("likes", []) + [_UserObjectId]
            result = self.core.InternalOperation("updatePost", {
                                                                "_id": _PostObjectid,
                                                                "new_values": {
                                                                    "likes": post["likes"],
                                                                    "date_modified"	 :	datetime.now()
                                                                }
                                                            }
                                             )
            # DICTIONARY (user, name, nick)
            dictionaryUser = {}
            for elem in result["likes"]:
                so = self.core.InternalOperation("getByIdUser", {"_id": elem})
                dictionaryUser[str(elem)] = {'name':so.pop("name"), 'nick':so.pop("nick")}
            #result["likes"] = self.core.InternalOperation("castListObjectsId2ListHexId", {"lis": result["likes"]})
            result["likes"] = dictionaryUser
            #result = self.core.InternalOperation("castDictDate2DateTimestamp", {"dictionary": result})
            #result = self.core.InternalOperation("castDictObjectsId2DictHexId", {"dictionary": result})
            return result
        except Exception, ex:
            print "Like has failed, " + ex.message