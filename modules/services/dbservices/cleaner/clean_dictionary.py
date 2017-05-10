# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class CleanDictionaryService(IService):
    def __init__(self, core, parameters):
        super(CleanDictionaryService, self).__init__(core, parameters)
    def run(self):

        dic = self.parameters.get("dic", {})
        keys =self.parameters.get("keys", [])
        return {x: dic[x] for x in dic if x not in keys}




