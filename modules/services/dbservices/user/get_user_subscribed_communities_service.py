# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetUserSubscribedCommunitiesService (IService):
    def __init__(self, core, parameters):
        super(GetUserSubscribedCommunitiesService, self).__init__(core, parameters)

    def run(self):
        user = self.core.InternalOperation("getByIdUser", {"_id": self.parameters["_id"]})
        communities_ids = user.get("communities_subscribed", [])
        if len(communities_ids) > 0:
            #communities = [self.retrieve_communities(elem_id) for elem_id in communities_ids]
            communities = [self.core.InternalOperation("getInfoCommunity", {"community_id": elem_id}) for elem_id in communities_ids]
            user["communities_subscribed"] = communities

        return user