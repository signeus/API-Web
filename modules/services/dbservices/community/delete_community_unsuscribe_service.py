# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class DeleteCommunityUnsuscribeService(IService):
    def __init__(self, core, parameters):
        super(DeleteCommunityUnsuscribeService, self).__init__(core, parameters)

    def run(self):
        result = DBService(self.core).updateMultiByFieldWithDelete('Users', self.parameters['field'], self.parameters['_id'])
        print '---------'
        print result
        print '---------'
        print 'Delete 2 Collection'
        result2 = DBService().deleteIn2Collection('Communities', self.parameters['_id'])
        print result2
        print '---------------'
        return result2
