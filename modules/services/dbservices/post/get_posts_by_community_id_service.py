# -*- coding: utf-8 -*-getPostsByCommunityId
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class GetPostsByCommunityIdService(IService):
    def __init__(self, core, parameters):
        super(GetPostsByCommunityIdService, self).__init__(core, parameters)

    def run(self):
        return DBService(self.core).getAllByFilter("Posts", self.parameters,  {'community_id':0})
