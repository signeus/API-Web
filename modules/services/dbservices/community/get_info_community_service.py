# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetInfoCommunityService (IService):
    def __init__(self, core, parameters):
        super(GetInfoCommunityService, self).__init__(core, parameters)

    def run(self):
        hide = ["leaders", "administrators", "invitations"]
        _ObjectId = self.parameters.get("community_id", "")
        _id = self.core.InternalOperation("castObjectId2Hex", {"id": _ObjectId})
        community = self.core.InternalOperation("getByIdCommunity", {"_id": _ObjectId})

        dic_clean = self.core.InternalOperation("cleanDictionary", {"dic": community, "keys": hide})

        return dic_clean

