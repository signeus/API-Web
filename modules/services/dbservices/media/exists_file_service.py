# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import os.path

class ExistsFileService(IService):
    def __init__(self, core, parameters):
        super(ExistsFileService, self).__init__(core, parameters)

    def run(self):
        try:
            filename = self.parameters.get("filename", 'default.png')
            relativePath = self.parameters.get("path", 'unknown/')
            path = self.core.GetMediaResources()["media_folder"] + relativePath

            if not os.path.exists(path):
                os.makedirs(path)
                print "Created directory in "+ path
            return os.path.isfile(path + filename)
        except Exception, ex:
            print "Failed the exists file checker."
            return 1

