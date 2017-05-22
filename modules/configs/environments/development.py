from configs.i_enviroment import IEnvironment

class Development(IEnvironment):
    def __init__(self):
        super(Development, self).__init__()
        self.configDict = {
                                'ip_database':'database',
                                'port_database':'27017',
                                'name_database':'kayoo',
                                'user_database': 'kaiser',
                                'psswd_database': 'kayoo1993',
                                'ip_app': 'kbdev',
                                'port_app':'8000',
                                'name_app':'kayoo',
                                'protocol_app':'http',
                                'media_folder':'/home/www/media/',
                                'ip_log_database':'database',
                                'name_log_database':'logKayoo',
                                'user_log_database': 'kaiser',
                                'psswd_log_database': 'kayoo1993',
                                'port_log_database':'27017'
                            }

    def config(self):
        return self.configDict