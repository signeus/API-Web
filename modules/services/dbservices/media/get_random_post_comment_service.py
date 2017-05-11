# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetRandomPostCommentService(IService):
    def __init__(self, core, parameters):
        super(GetRandomPostCommentService, self).__init__(core, parameters)

    def run(self):
        counts=DBService(self.core).getAllByFilter("Posts", {"$or":[{"post": {"$exists":True}}, {"comment": {"$exists":True}}]},
                                                   {"post":1,"comment":1,"_id":0})
        cnt=0
        wordsList=[]
        for i in counts:
            for k,v in i.iteritems():
                normal = self.core.InternalOperation("castDiacritics2Normalize", v)
                resul = self.core.InternalOperation("castSeparateText", normal)
                res = self.core.InternalOperation("castUrlEmailText", resul)
                dato= self.core.InternalOperation("castReplaceText", res)
                wordsList = wordsList + dato
        return wordsList