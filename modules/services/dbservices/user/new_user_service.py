# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewUserService (IService):
    def __init__(self, core, parameters):
        super(NewUserService, self).__init__(core, parameters)

    def run(self):
        image = self.parameters.get("avatar", None)
        self.parameters.pop("avatar", None)
        self.parameters["communities_subscribed"] = self.parameters.get("communities_subscribed",[])
        self.parameters["profile"] = self.parameters.get("profile",{})

        result = self.core.InternalOperation("createUser",self.parameters)
        if image:
            id = self.result.get("_id", None)
            if not id:
                raise Exception("New user, Not exists the ID to generate the image.")
            urlImage = self.core.InternalOperation("saveAvatar", {'id':id, 'data':image})
            result['image'] = urlImage

        return result