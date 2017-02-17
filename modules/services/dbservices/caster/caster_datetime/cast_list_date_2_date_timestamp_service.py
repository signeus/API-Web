# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class CastListDate2DateTimestampService (IService):
    def __init__(self, core, parameters):
        super(CastListDate2DateTimestampService, self).__init__(core, parameters)

    def run(self):
        lis = self.parameters.get("lis", None)
        for elem in lis:
            for key,value in elem.iteritems():
                if type(value).__name__ == "datetime":
                    elem[key] = value.strftime("%s")
        return lis