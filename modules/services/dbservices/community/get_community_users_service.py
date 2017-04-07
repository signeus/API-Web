# -*- coding: utf-8 -*-

from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetCommunityUsersService(IService):
    def __init__(self, core, parameters):
        super(GetCommunityUsersService, self).__init__(core, parameters)

    def run(self):
        id_comm = self.parameters["community_id"]
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": id_comm})
        return DBService(self.core).getAllByFilter("Users", {"communities_subscribed": {"$in": [_ObjectId]}})
