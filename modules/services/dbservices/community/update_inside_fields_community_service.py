# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class UpdateInsideFieldsCommunityService(IService):
    def __init__(self, core, parameters):
        super(UpdateInsideFieldsCommunityService, self).__init__(core, parameters)

    def run(self):
        return DBService(self.core).updateFieldInside("Communities", self.parameters["id"], self.parameters["field_path"], self.parameters["value"])