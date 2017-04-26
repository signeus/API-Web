# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SaveDefaultBannerService(IService):
    def __init__(self, core, parameters):
        super(SaveDefaultBannerService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "banners/"
        result = self.core.InternalOperation("saveDefaultBannerImage", self.parameters)
        if type(result) != str:
            return result
        return self.core.InternalOperation("getMediaRoute", {"service":"getBannerById", "attribs": {"id": result}})