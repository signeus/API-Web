# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class DeleteCommunityUnsubscribeService(IService):
    def __init__(self, core, parameters):
        super(DeleteCommunityUnsubscribeService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters['_id']
        result = DBService(self.core).updateMultiByFieldWithDelete('Users', self.parameters['field'], _id)
        result2 = self.core.InternalOperation("deleteCommunity", {'_id': _id})
        return result2
