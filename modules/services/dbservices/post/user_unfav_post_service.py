# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime

class UserUnfavPostService (IService):
    def __init__(self, core, parameters):
        super(UserUnfavPostService, self).__init__(core, parameters)

    def run(self):
        try:
            _UserObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["user_id"]})
            _PostObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id"]})
            post = self.core.InternalOperation("getPostById", {"id": self.parameters["id"]})
            if not _UserObjectId in post.get("favs", []):
                raise Exception("This user hasn't liked the post")


            resultUpdate = self.core.InternalOperation("extractInsideFieldsPost",
                                                       {"id": _PostObjectid, "field_path": "favs",
                                                        "value": _UserObjectId})

            post["favs"].remove(_UserObjectId)

            # DICTIONARY (user, name, nick)
            dictionaryUser = {}
            if post["favs"]:
                for elem in post["favs"]:
                    user = self.core.InternalOperation("getByIdUser", {"_id": elem})
                    dictionaryUser[str(elem)] = {'name':user.get("name", ""), 'nick':user.get("nick", "")}
                    post["favs"] = dictionaryUser
            else:
                post.pop("favs", "")

            return post
        except Exception, ex:
            print "Unfav has failed, " + ex.message