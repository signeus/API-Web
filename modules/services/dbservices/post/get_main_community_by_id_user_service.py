# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetMainCommunityByIdService(IService):
    def __init__(self, core, parameters):
        super(GetMainCommunityByIdService, self).__init__(core, parameters)

    def run(self):
        userId = self.parameters.get("user_id","")
        user = self.core.InternalOperation("getUserSubscribedCommunities", {"_id": userId})
        communities = user.get("communities_subscribed",[])
        if len(communities) == 0:
            return ""

        postsDict = {}
        for elem in communities:
            posts = self.core.InternalOperation("getCommunityPosts", {"community_id": elem['id'], "user_id": userId})
            for k, v in posts.iteritems():
                v["community_name"] = elem["name"] #Inserted the community name
                v["community_id"] = elem["id"] #Inserted the community ID
                postsDict[k] = v
        return postsDict
