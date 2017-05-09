# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class GetAllCommunitiesService(IService):
    def __init__(self, core, parameters):
        super(GetAllCommunitiesService, self).__init__(core, parameters)

    def run(self):
        invalid=[]
        dic_clean={}
        communities_to_show=[]
        _user_id = self.parameters.get("user_id",None)
        if not _user_id:
            raise Exception("Get All Communities: Empty user id is not allowed.")

        user = self.core.InternalOperation("getByIdUser", {"_id": _user_id})

        communities = self.core.InternalOperation("getAllCommunity", {})
        user_communities_subscribed = user.get("communities_subscribed",[])
        user_communities_requested = user.get("communities_requested",[])
        if len(user_communities_subscribed) > 0:
            for community in communities:
                if community["_id"] in user_communities_subscribed:
                    community["subscribed"] = True
                else:
                    community["subscribed"] = False
                if community.get("community_type",0) >0:
                    invalid=invalid+["description"]
                    if community["_id"] in user_communities_requested:
                        community["requested"] = True
                    else:
                        community["requested"] = False
                    if community["subscribed"]==False:
                        dic_clean=DBService(self.core).cleanDict(community,invalid)
                    else:

                        dic_clean=community

                _ObjectId = community.get("_id", "")
                _id = self.core.InternalOperation("castObjectId2Hex", {"id": _ObjectId})

                if _id:
                    dic_clean["members"] = self.core.InternalOperation("countCommunityMembers", {"community_id": _id})
                    dic_clean["banner"] = self.core.InternalOperation("getMediaRoute", {"service": "getBannerById",
                                                                                           "attribs": {"id": _id}})
                communities_to_show = communities_to_show + [dic_clean]

        return communities_to_show