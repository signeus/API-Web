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
        private_comm=[]
        _user_id = self.parameters.get("user_id",None)
        if not _user_id:
            raise Exception("Get All Communities: Empty user id is not allowed.")

        user = self.core.InternalOperation("getByIdUser", {"_id": _user_id})

        communities = self.core.InternalOperation("getAllCommunity", {})
        user_communities_subscribed = user.get("communities_subscribed",[])
        user_communities_requested = user.get("communities_requested",[])
        for community in communities:
            _ObjectId = community.get("_id", "")
            _id = self.core.InternalOperation("castObjectId2Hex", {"id": _ObjectId})

            if community.get("community_type", 0) == 1:
                private_comm=private_comm + [community.get("_id", "")]

            if community["_id"] in user_communities_subscribed:
                community["subscribed"] = True
            else:
                community["subscribed"] = False
                if community["_id"] in user_communities_requested:
                    community["requested"] = True
                else:
                    community["requested"] = False
            if community["_id"] in private_comm and community["subscribed"] == False:
                invalid = invalid + ["description"]
                dic_clean = self.core.InternalOperation("cleanDictionary", {"dic": community, "keys": invalid})
            else:
                dic_clean = community


            if _id:
                dic_clean["members"] = self.core.InternalOperation("countCommunityMembers", {"community_id": _id})
                dic_clean["banner"] = self.core.InternalOperation("getMediaRoute", {"service": "getBannerById",
                                                                                  "attribs": {"id": _id}})


            communities_to_show = communities_to_show + [dic_clean]

        return communities_to_show