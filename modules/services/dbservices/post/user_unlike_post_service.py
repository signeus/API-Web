# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime

class UserUnlike2PostService (IService):
    def __init__(self, core, parameters):
        super(UserUnlike2PostService, self).__init__(core, parameters)

    def run(self):
        try:
            _UserObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["user_id"]})
            _PostObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id"]})
            post = self.core.InternalOperation("getByIdPost", {"_id": self.parameters["id"]})
            if not _UserObjectId in post.get("likes", []):
                raise Exception("This user hasn't liked the post")


            resultUpdate = self.core.InternalOperation("extractInsideFieldsPost",
                                                       {"id": _PostObjectid, "field_path": "likes",
                                                        "value": _UserObjectId})

            post["likes"].remove(_UserObjectId)

            # DICTIONARY (user, name, nick)
            dictionaryUser = {}
            if post["likes"]:
                for elem in post["likes"]:
                    user = self.core.InternalOperation("getByIdUser", {"_id": elem})
                    dictionaryUser[str(elem)] = {'name':user.get("name", ""), 'nick':user.get("nick", "")}
                    post["likes"] = dictionaryUser
            else:
                post.pop("likes", "")

            return post
        except Exception, ex:
            print "Unlike has failed, " + ex.message