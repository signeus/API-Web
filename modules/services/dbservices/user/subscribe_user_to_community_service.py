# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SubscribeUser2Community (IService):
    def __init__(self, core, parameters):
        super(SubscribeUser2Community, self).__init__(core, parameters)

    def run(self):
        try:
            _creator = self.parameters.get("creator_id",None)
            _user_id = self.parameters.get("user_id",None)
            if not _user_id:
                raise Exception("Subscribe User to Community: Empty user_id not allowed.")

            user = self.core.InternalOperation("getByIdUser", {"_id":_user_id})
            _CommunityObjectid = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters.get("community_id", "")})

            community = self.core.InternalOperation("getByIdCommunity", {"_id":_CommunityObjectid})


            if (community.get("community_type", 0) > 0) and not _creator:
                raise Exception("Subscribe User to Community: Join to the private community is not allowed without permission.")

            result = self.core.InternalOperation("updateInsideFieldsUser",
                                                       {"id": user["_id"], "field_path": "communities_subscribed",
                                                        "value": _CommunityObjectid})
            community.pop("leaders",None)
            community.pop("invitations",None)
            community.pop("administrators",None)
            community.pop("creator_id",None)

            if result.get("nModified", 0) == 1:
                return community

        except Exception, ex:
            print "Subscribe User to Community has failed, " + ex.message
