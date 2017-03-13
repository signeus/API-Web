# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CheckOptionSurveyService (IService):
    def __init__(self, core, parameters):
        super(CheckOptionSurveyService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("id", None)
        _field = self.parameters.get("field", None)
        _user_id = self.parameters.get("user_id", None)
        if not _field:
            raise Exception("Empty option field in the survey not allowed.")

        return self.core.InternalOperation("updateInsideFieldsPost",
                                           {"id": _id, "field_path": "survey.answers." + str(_field),
                                            "value": _user_id})