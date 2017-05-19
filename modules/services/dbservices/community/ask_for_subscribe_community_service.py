# -*- coding: utf-8 -*-

from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class AskForSubscribeCommunityService(IService):
    def __init__(self, core, parameters):
        super(AskForSubscribeCommunityService, self).__init__(core, parameters)


    def run(self):
        community_id = self.parameters.get("community_id", "")
        user_id = self.parameters.get("user_id", "")
        community = self.core.InternalOperation("getByIdCommunity", {"_id": community_id})
        if community.get("community_type", 0) <> 1:
            raise Exception(" Action is not allowed for this Community Type.")
        user = self.core.InternalOperation("getByIdUser", {"_id": user_id})
        _community_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": community_id})
        user_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": user_id})
        if _community_ObjectId in user.get("communities_subscribed",0):
            raise Exception("User already subscribed in this Community")
        if user_ObjectId in community.get("requested", []):
            raise Exception("User subscription is waiting for validation in this Community")

        requests="requests"
        info =  self.core.InternalOperation("updateInsideFieldsCommunity",
                                              {"id": _community_ObjectId, "field_path": requests, "value": user_ObjectId})
        if info.get("nModified", 0) == 1:
            return {"user_id": user_id, "requested": True, "community_id": community_id}

        raise Exception("Request for subscription not completed")



