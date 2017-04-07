from configs.environments.development import Development
from configs.environments.production import Production
from configs.environments.dev_saray import DevSaray

class ResourceFactory (object):
    def __new__(cls, environmentName):
        resources = {
                        "development" : Development,
                        "dev_saray" : DevSaray,
                        "production": Production
                    }
        return resources[environmentName]()