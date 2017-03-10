# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastListDate2DateTimestampService (IService):
    def __init__(self, core, parameters):
        super(CastListDate2DateTimestampService, self).__init__(core, parameters)

    def run(self):
        return [{key:value.strftime("%s") for key,value in elem.iteritems() if type(value).__name__ == "datetime"} for elem in self.parameters.get("lis", [])]