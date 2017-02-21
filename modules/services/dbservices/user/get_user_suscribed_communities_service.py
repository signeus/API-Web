# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetUserSuscribedCommunities (IService):
    def __init__(self, core, parameters):
        super(GetUserSuscribedCommunities, self).__init__(core, parameters)

    def run(self):
        user = self.core.InternalOperation("getByIdUser", {"_id": self.parameters["_id"]})
        communities_ids = user.get("communities_suscribed", [])
        if len(communities_ids) > 0:
            communities = [self.retrieve_communities(elem_id) for elem_id in communities_ids]
            user["communities_suscribed"] = communities
        return user

    def retrieve_communities(self, id):
        community = self.core.InternalOperation("getByIdCommunity", {"_id":id})
        lite_community = {}
        lite_community["id"] = community["_id"]
        lite_community["name"] = community["name"]
        lite_community["banner"] = self.core.InternalOperation("getMediaRoute", {"service": "getBannerById",
                                                                                "attribs": {"id": str(id)}})
        order = community.get("order", [])
        if order:
            lite_community["order"] = order
        return lite_community
