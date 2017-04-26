# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastDate2DateTimestampService (IService):
    def __init__(self, core, parameters):
        super(CastDate2DateTimestampService, self).__init__(core, parameters)

    def run(self):
        dateObject = self.parameters.get("date", None)
        return int(dateObject.strftime("%s"))

