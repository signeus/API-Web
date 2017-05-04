# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import json

class NewSurveyAnswerService (IService):
    def __init__(self, core, parameters):
        super(NewSurveyAnswerService, self).__init__(core, parameters)

    def run(self):

        post_id = self.parameters["post_id"]
        user_id = self.core.InternalOperation("castHex2ObjectId", {"id": self.parameters["user_id"]})
        ans = self.parameters["answer_id"]
        answer="survey.answers." + ans
        post=DBService(self.core).updateFieldInside("Posts", post_id, answer, user_id)
        dic_post = {"post_id": post_id}
        if post:
            post=DBService(self.core).getById("Posts", post_id)
            print post
            for i in post.iteritems():
                if i[0] == "survey":
                    for k, v in i[1].iteritems():
                        if k=="answers":
                            res={"answers":v}
                            break

        resul = dict(dic_post, **res)
        return resul