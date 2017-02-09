# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetAvatarByIdLegacyService(IService):
    def __init__(self, core, parameters):
        super(GetAvatarByIdLegacyService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        try:
            _id = self.parameters.get("_id", '0')
            name = _id + self.core.FilesOperation("getFileTypeService",{"type":"images","ext":"png"})
            #myfile = io.BytesIO(open("/home/kevin/Pictures/avatares/" + name, "rb", buffering=0).read())
            #myfile = io.BytesIO(open("/home/kevin/Pictures/avatares/" + name, "rb").read())
            myfile = "/home/kevin/Pictures/avatares/" + name
            return myfile
        except Exception, ex:
            print ex.message
