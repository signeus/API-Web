# -*- coding: utf-8 -*-

from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class AdminManageSubscriptionsService(IService):
    def __init__(self, core, parameters):
        super(AdminManageSubscriptionsService, self).__init__(core, parameters)


    def run(self):
        validators = []
        community_id = self.parameters.get("community_id", "")
        user_id = self.parameters.get("user_id", "")
        request_user = self.parameters.get("request_user", "")
        subscription = self.parameters.get("subscription", "")
        community = self.core.InternalOperation("getByIdCommunity", {"_id": community_id})
        validators= community.get("administrators", []) + community.get("leaders", [])

        if user_id not in validators :
            raise Exception("Your User has not permissions to validate subscriptions")

        _request_user_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": request_user})

        if _request_user_ObjectId not in community.get("requests", []):
            raise Exception("This user has not requested a subscriptions for this community")

        user = self.core.InternalOperation("getByIdUser", {"_id": request_user})
        _community_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": community_id})

        if _community_ObjectId in user.get("communities_subscribed", 0):
            raise Exception("User already subscribed in this Community")

        if subscription == True:
            action = "communities_subscribed"
            result = self.core.AdminOperation("adminAcceptSubscription",
                                              {"request_user": _request_user_ObjectId, "field": action,
                                                "community_id": _community_ObjectId})
            return result

        else:
            action = "communities_rejected"
            result = self.core.AdminOperation("adminAcceptSubscription",
                                              {"request_user": _request_user_ObjectId, "field": action,
                                               "community_id": _community_ObjectId})
            return result


