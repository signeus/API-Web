# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService


class FindService(IService):
    def __init__(self, core, parameters):
        super(FindService, self).__init__(core, parameters)

    def run(self):
        foundUser = self.core.InternalOperation("findUser", self.parameters)
        foundCommunity = self.core.InternalOperation("findCommunity", self.parameters)
        foundPost = self.core.InternalOperation("findPost", self.parameters)
        allFound=dict(foundUser, **foundPost)
        allFound.update(foundCommunity)
        return allFound
