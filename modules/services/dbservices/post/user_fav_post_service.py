# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime

class UserFavPostService (IService):
    def __init__(self, core, parameters):
        super(UserFavPostService, self).__init__(core, parameters)

    def run(self):
        try:
            _UserObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["user_id"]})
            _PostObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["id"]})
            post = self.core.InternalOperation("getPostById", {"id": self.parameters["id"]})
            if _UserObjectId in post.get("favs", []):
                raise Exception('This user already liked the post')

            post["favs"] = post.get("favs", []) + [_UserObjectId]

            resultUpdate = self.core.InternalOperation("updateInsideFieldsPost",
                                               {"id": _PostObjectid, "field_path": "favs",
                                                "value": _UserObjectId})

            # DICTIONARY (user, name, nick)
            dictionaryUser = {}
            for elem in post["favs"]:
                user = self.core.InternalOperation("getByIdUser", {"_id": elem})
                dictionaryUser[str(elem)] = {'name':user.get("name", ""), 'nick':user.get("nick", "")}
            post["favs"] = dictionaryUser
            return post
        except Exception, ex:
            print "Fav has failed, " + ex.message