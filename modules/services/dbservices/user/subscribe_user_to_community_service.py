# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SubscribeUser2Community (IService):
    def __init__(self, core, parameters):
        super(SubscribeUser2Community, self).__init__(core, parameters)

    def run(self):
        #Retrieve the data about user and community.
        _community = self.parameters.get("community", {})
        _user = self.parameters.get("user", {})
        _creator = self.parameters.get("creator_id","")

        #Check if the community is not public or User is not the creator.
        if (_community.get("community_type", 0) > 0) and not _creator:
            raise Exception("It is not allowed to subscribe to the non-public community.")

        result = self.core.InternalOperation("updateInsideFieldsUser",
                                                   {"id": _user["_id"], "field_path": "communities_subscribed",
                                                    "value": _community["_id"]})

        #Inserting the User Id inside Communities Subscribe
        _user["communities_subscribed"] = _user["communities_subscribed"] +  [_community["_id"]]
        _community.pop("leaders",None)
        _community.pop("invitations",None)
        _community.pop("administrators",None)
        _community.pop("creator_id",None)

        #Correct and modified.
        if result.get("nModified", 0) == 1:
            return _community

