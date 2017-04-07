# -*- coding: utf-8 -*-

from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class CountCommunityMembersService(IService):
    def __init__(self, core, parameters):
        super(CountCommunityMembersService, self).__init__(core, parameters)


    def run(self):
        id_comm=self.parameters["community_id"]
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": id_comm})

        counts = DBService(self.core).countFields("Users",
                                                  {"communities_subscribed": { "$in":[_ObjectId] }})
        communityCount={}
        communityCount["Count"]=counts
        return communityCount