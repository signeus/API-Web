from configs.i_enviroment import IEnvironment

class DevSaray(IEnvironment):
    def __init__(self):
        super(DevSaray, self).__init__()
        self.configDict = {
                                'ip_database':'kbdev',
                                'port_database':'27017',
                                'name_database':'warehouse',
                                'user_database': 'kayoo',
                                'psswd_database': '-',
                                'ip_app': '10.0.40.92',
                                'port_app':'8000',
                                'name_app':'kayoo',
                                'protocol_app':'http',
                                'media_folder':'/home/www/media/',
                                'ip_log_database':'kbdev',
                                'name_log_database':'logKayoo',
                                'port_log_database':'27017',
                                'user_log_database': 'kayoo',
                                'psswd_log_database': '-',
                            }

    def config(self):
        return self.configDict