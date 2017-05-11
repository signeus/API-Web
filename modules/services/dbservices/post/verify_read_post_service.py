# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

#parameters=community_id, user_id
class VerifyReadPostService (IService):
    def __init__(self, core, parameters):
        super(VerifyReadPostService, self).__init__(core, parameters)

    def run(self):
        post_id=self.parameters.get("post_id", "")
        us_id = self.parameters.get("user_id", "")
        values = {"id":post_id, "user.id": us_id, "action":"readPost"}
        read=DBService(self.core).getAllByFilter("actions", values, {}, "log")
        if len(read)>0:
            resul=True
            return resul
        return False