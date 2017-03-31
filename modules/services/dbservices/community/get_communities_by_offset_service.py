# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetCommunitiesByOffsetService(IService):
    def __init__(self, core, parameters):
        super(GetCommunitiesByOffsetService, self).__init__(core, parameters)

    def run(self):
        return DBService(self.core).getNextFields("Communities", self.parameters["start"], self.parameters["offset"])
