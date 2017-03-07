# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import io
from PIL import Image
import time

class GetAvatarByIdService(IService):
    def __init__(self, core, parameters):
        super(GetAvatarByIdService, self).__init__(core, parameters)

    def run(self):
        self.parameters["path"] = "avatars/"
        return self.core.InternalOperation("getDirImageById", self.parameters)