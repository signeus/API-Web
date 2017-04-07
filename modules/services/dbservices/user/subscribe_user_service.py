# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class SubscribeUserService (IService):
    def __init__(self, core, parameters):
        super(SubscribeUserService, self).__init__(core, parameters)

    def run(self):
        return self.core.InternalOperation("subscribeUser2Community", self.parameters) if self.parameters["status"] else self.core.InternalOperation("unsubscribeUser2Community", self.parameters)