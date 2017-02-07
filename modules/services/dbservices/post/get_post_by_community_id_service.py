# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class GetPostByCommunityId(IService):
    def __init__(self, core, parameters):
        super(GetPostByCommunityId, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        print self.parameters
        return DBService().getAllByFilter("Posts", self.parameters)
