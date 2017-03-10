# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CheckOptionSurveyService (IService):
    def __init__(self, core, parameters):
        super(CheckOptionSurveyService, self).__init__(core, parameters)

    def run(self):
        return ""