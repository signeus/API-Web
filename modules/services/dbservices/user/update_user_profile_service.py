# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class UpdateUserProfileService (IService):
    def __init__(self, core, parameters):
        super(UpdateUserProfileService, self).__init__(core, parameters)

    def run(self):
        print self.parameters
        _id = self.parameters.get("id", "")
        name = self.parameters.get("firstName", "")
        lastName = self.parameters.get("lastName", "")
        mail = self.parameters.get("email", "")
        avatar = self.parameters.get("profileImage", "")
        nick = "" ##Autogenerate FirstName.LastName

        if mail == "":
            raise Exception("Empty email is not allowed.")

        if name == "":
            raise Exception("Empty name is not allowed.")

        newLis = self.parameters
        newLis.pop("id", None)
        newLis.pop("firstName", None)
        newLis.pop("email", None)
        newLis.pop("profileImage", None)
        newLis.pop("nick", None)
        nick = name + "." + lastName

        result = self.core.InternalOperation("updateUser", {"_id":_id, "new_values":{"name":name, "mail":mail, "nick":nick, "profile":newLis}})
        if avatar:
            avatar = self.core.InternalOperation("saveAvatar", {"id": _id, "data": avatar})
            result["avatar"] = avatar

        return result