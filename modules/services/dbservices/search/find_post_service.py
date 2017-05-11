# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class FindPostService(IService):
    def __init__(self, core, parameters):
        super(FindPostService, self).__init__(core, parameters)

    def run(self):
        resul= DBService(self.core).findIn("Posts", ["post","repost", "comment"], self.parameters["search"])
        return {"posts":resul}

