# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class UnsubscribeUser2Community (IService):
    def __init__(self, core, parameters):
        super(UnsubscribeUser2Community, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        try:
            user = self.core.InternalOperation("getByIdUser", {"_id": self.parameters.get("user_id", "")})
            _communityId = self.parameters.get("community_id", "")
            _CommunityObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": _communityId})
            result = self.core.InternalOperation("extractInsideFieldsUser",
                                                       {"id": user["_id"], "field_path": "communities_subscribed",
                                                        "value": _CommunityObjectid})
            if result.get("nModified", 0) == 1:
                return {"id":_CommunityObjectid}

        except Exception, ex:
            print "Unsubscribe User to Community has failed, " + ex.message
