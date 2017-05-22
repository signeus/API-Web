# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SubscribeUserService (IService):
    def __init__(self, core, parameters):
        super(SubscribeUserService, self).__init__(core, parameters)

    def run(self):
        #Retrieve user and community data
        _user_id = self.parameters.get("user_id",None)
        _community_id = self.parameters.get("community_id", None)
        if not _user_id or not _community_id:
            raise Exception("Values doesn't allowed")


        community = self.core.InternalOperation("getByIdCommunity", {"_id": _community_id})
        user = self.core.InternalOperation("getByIdUser", {"_id": _user_id})

        communitiesSubscribed = user.get("communities_subscribed", "")
        _UserObjectId = user.get("_id", None)
        _CommunityObjectid = community.get("_id", None)

        if not _UserObjectId or not _CommunityObjectid:
            raise Exception("There is an issue with Community Id or User Id, please contact with tech support")

        self.parameters["community"] = community
        self.parameters["user"] = user
        ObjectId("5922d70f4186232c22f1cf67")
        if communitiesSubscribed > 0:
            if _CommunityObjectid in communitiesSubscribed:
                return self.core.InternalOperation("unsubscribeUser2Community", self.parameters)

        return self.core.InternalOperation("subscribeUser2Community", self.parameters)