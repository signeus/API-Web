# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastDictDate2DateTimeStampService (IService):
    def __init__(self, core, parameters):
        super(CastDictDate2DateTimeStampService, self).__init__(core, parameters)

    def run(self):
        return {key: value.strftime("%s") for key, value in self.parameters.get("dictionary", {}).iteritems() if type(value).__name__ == "datetime"}