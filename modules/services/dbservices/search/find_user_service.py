# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class FindUserService(IService):
    def __init__(self, core, parameters):
        super(FindUserService, self).__init__(core, parameters)

    def run(self):
        resul= DBService(self.core).findIn("Users", ["name","nick", "mail"], self.parameters["search"])
        [i.pop("psswd","") for i in resul]
        return {"users":resul}
