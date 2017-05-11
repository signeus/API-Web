# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class UpdateInsideFieldsUserService(IService):
    def __init__(self, core, parameters):
        super(UpdateInsideFieldsUserService, self).__init__(core, parameters)

    def run(self):
        return DBService(self.core).updateFieldInside("Users", self.parameters["id"], self.parameters["field_path"], self.parameters["value"])