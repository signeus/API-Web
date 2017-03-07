# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from resources_manager.media.media_enrouting import MediaEnrouting

class GetMediaRoute(IService):
    def __init__(self, core, parameters):
        super(GetMediaRoute, self).__init__(core, parameters)

    def run(self):
        try:
            serviceName = self.parameters.get("service", 'nonService')
            attribs = self.parameters.get("attribs", {})
            url = MediaEnrouting(self.core.rm.MediaManager()).getMedia2External("media/" + serviceName, attribs)
            return url
        except Exception, ex:
            print ex.message