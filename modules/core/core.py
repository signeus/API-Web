# -*- coding: utf-8 -*-
from services.service_factory import ServiceFactory
from resources_manager.resource_manager import ResourceManager

class Core:
    def __init__(self):
        self.rm = ResourceManager(self)

    def UserOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters)

    def CommunityOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters)

    def PostOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters)

    def MediaOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters)

    def FilesOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters)

    def InternalOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters, True)

    def FactoryOperation(self, serviceName, parameters, internalContext=False):
        try:
            return ServiceFactory(serviceName, self, parameters).run()
        except Exception, ex:
            print '------'
            print ex
            print '------'
            return {"result":1, "message":ex.message}

    def GetMediaResources(self):
        try:
            return self.rm.MediaManager()
        except Exception, ex:
            return ex.message

    def GetDatabaseResources(self):
        try:
            return self.rm.DatabaseManager()
        except Exception, ex:
            return ex.message