# -*- coding: utf-8 -*-

from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class AdminRejectSubscriptionService(IService):
    def __init__(self, core, parameters):
        super(AdminRejectSubscriptionService, self).__init__(core, parameters)


    def run(self):
        _community_ObjectId = self.parameters.get("community_id", "")
        _request_user_ObjectId = self.parameters.get("request_user", "")
        action = self.parameters.get("field", "")
        info = self.core.InternalOperation("updateInsideFieldsUser",
                                           {"id": _request_user_ObjectId, "field_path": action,
                                            "value": _community_ObjectId})
        if info.get("nModified", 0) == 1:
            return {"request_user": request_user, "subscription": False, "community_id": community_id}
