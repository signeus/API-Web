# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetInfoCommunityService (IService):
    def __init__(self, core, parameters):
        super(GetInfoCommunityService, self).__init__(core, parameters)

    def run(self):
        hide = ["leaders", "administrators", "invitations"]
        _ObjectId = self.parameters.get("community_id", "")
        community = self.core.InternalOperation("getByIdCommunity", {"_id": _ObjectId})
        if community:
            community["id"] = community.pop("_id", None)

        dic_clean = self.core.InternalOperation("cleanDictionary", {"dic": community, "keys": hide})

        return dic_clean
