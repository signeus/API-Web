# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetUserSuscribedCommunities (IService):
    def __init__(self, core, parameters):
        super(GetUserSuscribedCommunities, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        user = self.core.UserOperation("getByIdUser", {"_id": self.parameters["_id"]})
        communities_ids = user.get("communities_suscribed", [])
        if len(communities_ids) <= 0:
            return "FCK"
        result = [self.retrieve_communities(elem_id) for elem_id in communities_ids]
        user["communities_suscribed"] = result
        return user

    def retrieve_communities(self, id):
        community = self.core.CommunityOperation("getByIdCommunity", {"_id":id})
        lite_community = {}
        lite_community["id"] = community["_id"]
        lite_community["name"] = community["name"]
        order = community.get("order", [])
        if order:
            lite_community["order"] = order
        return lite_community
