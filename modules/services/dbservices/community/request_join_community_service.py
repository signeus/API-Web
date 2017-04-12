# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class RequestJoinCommunityService (IService):
    def __init__(self, core, parameters):
        super(RequestJoinCommunityService, self).__init__(core, parameters)

    def run(self):
        _user_id = self.parameters.get("user_id", None)
        if not _user_id:
            raise Exception("Request user to Community: Empty user_id not allowed.")

        user = self.core.InternalOperation("getByIdUser", {"_id": _user_id})
        _CommunityObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters.get("community_id", "")})

        result = self.core.InternalOperation("updateInsideFieldsUser",
                                             {"id": user["_id"], "field_path": "communities_requested",
                                              "value": _CommunityObjectid})

        if result.get("nModified", 0) == 1:
            return {"id": _CommunityObjectid}
