import socket
from configs.i_enviroment import IEnvironment

class Production(IEnvironment):
    def __init__(self):
        super(Production, self).__init__()
        externalIp = str([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
        self.configDict = {
                                'ip_database':'database',
                                'port_database':'27017',
                                'name_database':'kayoo',
                                'ip_app': externalIp,
                                'port_app':'8000',
                                'name_app':'kayoo',
                                'protocol_app':'http',
                                'media_folder':'/home/www/media/',
                                'ip_log_database':'database',
                                'name_log_database':'logKayoo',
                                'port_log_database':'27017'
                            }

    def config(self):
        return self.configDict