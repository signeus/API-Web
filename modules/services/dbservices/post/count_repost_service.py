# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CountRepostService(IService):
    def __init__(self, core, parameters):
        super(CountRepostService, self).__init__(core, parameters)


    def run(self):
        print self.parameters ##This is equal to your old "Request vars"
        return "count repost by post_id"