# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class FindCommunityService(IService):
    def __init__(self, core, parameters):
        super(FindCommunityService, self).__init__(core, parameters)

    def run(self):
        resul= DBService(self.core).findIn("Communities", ["name","description", "keywords"], self.parameters["search"])
        return {"communities":resul}

