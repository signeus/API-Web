from resource_factory import ResourceFactory
from configs.environment import env

class ResourceManager:
    def __init__(self, core):
        self.environmentName = env
        self.core = core

    def MediaManager(self):
        return self.ManagerOperation(self.environmentName)

    def DatabaseManager(self):
        return self.ManagerOperation(self.environmentName)

    def ManagerOperation(self, environmentName):
        try:
            return ResourceFactory(environmentName).config()
        except Exception, ex:
            return ex.message