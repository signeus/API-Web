# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class ExistsUrlService (IService):
    def __init__(self, core, parameters):
        super(ExistsUrlService, self).__init__(core, parameters)

    def run(self):
        url = self.parameters.get("url", None)
        if not url:
            return False

        import urllib2
        try:
            urllib2.urlopen(url)
        except Exception, e:
            return False


        return True
