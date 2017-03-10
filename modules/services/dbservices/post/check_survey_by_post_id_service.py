# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from datetime import datetime
from services.dbservices.db_service import DBService

class CheckSurveyByPostIdService (IService):
    def __init__(self, core, parameters):
        super(CheckSurveyByPostIdService, self).__init__(core, parameters)

    def run(self):
        try:
            _user_id = self.parameters.get("user_id", None)
            _post_id = self.parameters.get("id", None)
            _answers = self.parameters.get("answers", {})
            _multicheck = self.parameters.get("multicheck", False)

            if not _multicheck and len(_answers) > 1:
                raise Exception("Multi checks is not allowed in this post.")

            _post_object_id = self.core.InternalOperation("castHex2ObjectId", {"id": _post_id})
            _user_object_id = self.core.InternalOperation("castHex2ObjectId", {"id": _user_id})
            post = self.core.InternalOperation("getByIdPost", {"_id": _post_object_id})

            userChecked = []
            newChecks = []

            originalAnswers =  post.get("survey",{}).get("answers",None)

            if not originalAnswers:
                raise Exception("There aren't answers for this post.")

            for answer in _answers:
                if _user_object_id in originalAnswers[answer]:
                    userChecked.append(answer)
                else:
                    newChecks.append(answer)

            if len(userChecked) > 0:
                print "Preguntas enviadas en las que se encuentra el usuario para desmarcar: "
                print userChecked

            if len(newChecks) > 0:
                print "Preguntas enviadas para marcar: "
                return DBService(self.core).updateFieldInside("Posts", {'id':_post_object_id}, {'newValues':''})
                print newChecks

            return "OK"
        except Exception, ex:
            print "Check survey has failed, " + ex.message