# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import io
from PIL import Image
import time

class GetBannerByIdService(IService):
    def __init__(self, core, parameters):
        super(GetBannerByIdService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "banners/"
        return self.core.InternalOperation("getDirImageById", self.parameters)