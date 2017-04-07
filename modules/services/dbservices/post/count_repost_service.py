# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService



class CountRepostService(IService):
    def __init__(self, core, parameters):
        super(CountRepostService, self).__init__(core, parameters)


    def run(self):

        counts=DBService(self.core).countFields("Posts", {"repost": {"$exists": True}, "post_id": self.parameters['post_id']})
        #counts = DBService(self.core).countFields("Users",
        #                                         {"name": "Saray"})
        repostCount={}
        repostCount["Count"]=counts
        return repostCount

