# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class FavPostService (IService):
    def __init__(self, core, parameters):
        super(FavPostService, self).__init__(core, parameters)

    def run(self):
        return self.core.InternalOperation("userFavPost", self.parameters) if self.parameters["status"] else self.core.InternalOperation("userUnfavPost", self.parameters)