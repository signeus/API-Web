from configs.i_enviroment import IEnvironment

class Development(IEnvironment):
    def __init__(self):
        super(Development, self).__init__()
        self.configDict = {
                                'ip_database':'127.0.0.1',
                                'port_database':'27017',
                                'name_database':'warehouse',
                                'ip_app': 'kbdev',
                                'port_app':'8000',
                                'name_app':'kayoo',
                                'protocol_app':'http',
                                'media_folder':'/home/www/media/',
                                'ip_log_database':'127.0.0.1',
                                'name_log_database':'logKayoo',
                                'port_log_database':'27017'
                            }

    def config(self):
        return self.configDict