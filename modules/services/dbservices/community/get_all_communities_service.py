# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetAllCommunitiesService(IService):
    def __init__(self, core, parameters):
        super(GetAllCommunitiesService, self).__init__(core, parameters)

    def run(self):
        _user_id = self.parameters.get("user_id",None)
        if not _user_id:
            raise Exception("Get All Communities: Empty user id is not allowed.")

        user = self.core.InternalOperation("getByIdUser", {"_id": _user_id})

        communities = self.core.InternalOperation("getAllCommunity", {})
        user_communities = user.get("communities_subscribed",[])
        if len(user_communities) > 0:
            for community in communities:
                if community["_id"] in user_communities:
                    community["subscribed"] = True
                else:
                    community["subscribed"] = False
        return communities