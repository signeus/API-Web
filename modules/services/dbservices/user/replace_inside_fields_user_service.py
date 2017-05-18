# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class ReplaceInsideFieldsUserService(IService):
    def __init__(self, core, parameters):
        super(ReplaceInsideFieldsUserService, self).__init__(core, parameters)

    def run(self):
        return DBService(self.core).replaceFieldInside("Users", self.parameters["id"], self.parameters["field_path"], self.parameters["value"])