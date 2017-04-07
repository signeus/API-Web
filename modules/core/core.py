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

    def SearchOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters)

    def InternalOperation(self, serviceName, parameters):
        return self.FactoryOperation(serviceName, parameters, True)

    def FactoryOperation(self, serviceName, parameters, internalContext=False):
        try:
            serviceResult = ServiceFactory(serviceName, self, parameters).run()
            if not internalContext:
                resultDict = {}
                resultDict["data"] = serviceResult
                resultDict['result'] = 0
                return resultDict
            return serviceResult
        except Exception, ex:
            print '------'
            print ex
            print type(ex)
            print '------'
            return {"result":1, "data":{"message":ex.message, "error":1, "type": 1}}

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