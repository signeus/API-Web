# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime

class Unlike2PostService (IService):
    def __init__(self, core, parameters):
        super(Unlike2PostService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        try:
            _UserObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id_user"]})
            _PostObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id"]})
            post = self.core.PostOperation("getByIdPost", {"_id": self.parameters["id"]})
            if not _UserObjectId in post["likes"]:
                raise Exception("This user hasn't liked the post")

            post["likes"] = post.get("likes", []).remove(_UserObjectId)
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
            result = self.core.InternalOperation("castDictDate2DateTimestamp", {"dictionary": result})
            result = self.core.InternalOperation("castDictObjectsId2DictHexId", {"dictionary": result})
            return result
        except Exception, ex:
            print "Like has failed, " + ex.message