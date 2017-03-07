# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewCommunityService (IService):
    def __init__(self, core, parameters):
        super(NewCommunityService, self).__init__(core, parameters)

    def run(self):
        image = self.parameters.get("banner", None)
        self.parameters.pop("banner", None)

        record = self.core.InternalOperation("createCommunity",self.parameters)
        result = self.core.InternalOperation("suscribeUser2Community",
                                             {"id_user": record["id_creator"], "id_community": record["_id"]})
        if image:
            id = self.result.get("_id", None)
            if not id:
                raise Exception("New community, Not exists the ID to generate the image.")
            urlImage = self.core.InternalOperation("saveBanner", {'id':id, 'data':image})
            result['image'] = urlImage

        return result