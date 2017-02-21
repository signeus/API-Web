# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetAvatarByIdLegacyService(IService):
    def __init__(self, core, parameters):
        super(GetAvatarByIdLegacyService, self).__init__(core, parameters)

    def run(self):
        try:
            _id = self.parameters.get("_id", '0')
            name = _id + self.core.InternalOperation("getFileTypeService",{"type":"images","ext":"png"})
            myfile = "/home/www/media/avatars/" + name
            return myfile
        except Exception, ex:
            print ex.message
