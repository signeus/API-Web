# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class castDate2DateTimeStamp (IService):
    def __init__(self, core, parameters):
        super(castDate2DateTimeStamp, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        dateObject = self.parameters.get("date", None)
        return int(dateObject.strftime("%s"))

