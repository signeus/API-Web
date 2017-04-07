from configs.i_enviroment import IEnvironment

class DevSaray(IEnvironment):
    def __init__(self):
        super(DevSaray, self).__init__()
        self.configDict = {
                                'ip_database':'kbdev',
                                'port_database':'27017',
                                'name_database':'warehouse',
                                'ip_app': 'localhost',
                                'port_app':'8000',
                                'name_app':'kayoo',
                                'protocol_app':'http',
                                'media_folder':'/home/www/media/'
                            }

    def config(self):
        return self.configDict