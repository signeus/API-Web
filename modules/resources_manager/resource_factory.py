from configs.environments.development import Development

class ResourceFactory (object):
    def __new__(cls, environmentName):
        resources = {
                        "development" : Development
                    }
        return resources[environmentName]()