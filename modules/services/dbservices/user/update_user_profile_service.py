# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class UpdateUserProfileService (IService):
    def __init__(self, core, parameters):
        super(UpdateUserProfileService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", "")
        name = self.parameters.get("name", "")
        firstName = self.parameters.get("firstName", "")
        lastName = self.parameters.get("lastName", "")
        mail = self.parameters.get("email", "")
        avatar = self.parameters.get("profileImage", "")
        alias = "" ##Autogenerate FirstName.LastName

        if mail == "":
            raise Exception("Empty email is not allowed.")

        if name == "":
            raise Exception("Empty name is not allowed.")

        newLis = self.parameters
        newLis.pop("id", None)
        newLis.pop("name", None)
        newLis.pop("email", None)
        newLis.pop("profileImage", None)
        newLis.pop("alias", None)
        newLis.pop("psswd", None)
        alias = firstName + "." + lastName

        result = self.core.InternalOperation("updateUser", {"_id":_id, "new_values":{"name":name, "mail":mail, "alias":alias, "profile":newLis}})
        if avatar:
            avatar = self.core.InternalOperation("saveAvatar", {"id": _id, "data": avatar})
            result["avatar"] = avatar

        return result