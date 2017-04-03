# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetUserFormatByIdService(IService):
    def __init__(self, core, parameters):
        super(GetUserFormatByIdService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("user_id","")

        users = self.core.InternalOperation("getAllUsersFiltered", {'query': {}, 'filter': {'name': 1, 'nick': 1}})

        return users[str(_id)]