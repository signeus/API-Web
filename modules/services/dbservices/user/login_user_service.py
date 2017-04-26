# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class LoginUserService (IService):
    def __init__(self, core, parameters):
        super(LoginUserService, self).__init__(core, parameters)

    def run(self):
        _mail = self.parameters.get("mail","")
        _psswd = self.parameters.get("psswd", "")
        if _mail == "" or _psswd  == "":
            raise Exception("Empty required field, password or username")
        _user = self.core.InternalOperation("getAllUsersFiltered", {'query':{"mail":_mail,"psswd":_psswd}, 'filter':{"psswd":0}})
        if not _user:
            raise Exception("No matches found")
        keys = _user.keys()
        if keys <= 0:
            raise Exception("I don't have the user_id")
        user2Render = self.core.InternalOperation("getUserSubscribedCommunities", {"_id": keys[0]})
        user2Render.pop("psswd")

        return user2Render
