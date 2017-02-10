from configs.i_enviroment import IEnvironment

class Development(IEnvironment):
    def __init__(self):
        super(Development, self).__init__()
        self.configDict = {
                                'ip_database':'127.0.0.1',
                                'port_database':'27017',
                                'name_database':'warehouse',
                                'ip_app': '192.168.1.176',
                                'port_app':'8001',
                                'application':'kayoo2'
                            }

    def config(self):
        return self.configDict