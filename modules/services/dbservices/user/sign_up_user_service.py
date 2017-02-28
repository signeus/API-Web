# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SignUpUserService (IService):
    def __init__(self, core, parameters):
        super(SignUpUserService, self).__init__(core, parameters)

    def run(self):
        _mail = self.parameters.get("mail","")
        _psswd = self.parameters.get("psswd", "")
        _user_name = self.parameters.get("name", "")
        if _mail == "" or _psswd  == "":
            raise Exception("Empty required field, password or username")
        _user = self.core.InternalOperation("getAllUsersFiltered", {'query':{"mail":_mail}, 'filter':{"psswd":0}})
        if _user:
            raise Exception("There is a user with that email")
        _user_created = self.core.InternalOperation("createUser", {"name":_user_name, "psswd":_psswd, "mail":_mail })
        _user_created.pop("psswd")
        return _user_created
