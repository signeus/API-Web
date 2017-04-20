# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetInfoCommunityService (IService):
    def __init__(self, core, parameters):
        super(GetInfoCommunityService, self).__init__(core, parameters)

    def run(self):
        _ObjectId = self.parameters.get("community_id", "")
        _id = self.core.InternalOperation("castObjectId2Hex", {"id": _ObjectId})

        community = self.core.InternalOperation("getByIdCommunity", {"_id": _ObjectId})
        lite_community = {}
        lite_community["id"] = community["_id"]
        lite_community["name"] = community.get("name", "")
        lite_community["description"] = community.get("description", "")
        lite_community["banner"] = self.core.InternalOperation("getMediaRoute", {"service": "getBannerById",
                                                                                 "attribs": {"id": _id}})

        lite_community["members"] = self.core.InternalOperation("countCommunityMembers", {"community_id": _id})
        return lite_community