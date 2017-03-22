# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import sys, os

class IdentifyExternalUrlService (IService):
    def __init__(self, core, parameters):
        super(IdentifyExternalUrlService, self).__init__(core, parameters)

    def run(self):
        _url = self.parameters.get("link", "")
        try:
            types_allowed = {

                                'youtube' : {'name':'youtube','id': _url[_url.find('watch?v='):].split('=')[1] if _url.find('watch?v=') >= 0 else ""},
                                'vimeo'   : {'name':'vimeo','id': _url[_url.rfind('/') + 1:] if _url.rfind('/') >= 0 else ""},
                                'twitch.tv/videos' : {'name':'twitch.video','id': _url[_url.rfind('/') + 1:] if _url.rfind('/') >= 0 else ""},
                                'twitch' : {'name':'twitch','id': _url[_url.rfind('/') + 1:] if _url.rfind('/') >= 0 else ""},
                                'dailymotion' : {'name':'dailymotion','id': _url[_url.rfind('/') + 1:] if _url.rfind('/') >= 0 else ""},
                                'gaming.youtube': {'name': 'gaming.youtube', 'id': _url[_url.find('watch?v='):].split('=')[1] if _url.find( 'watch?v=') >= 0 else ""},
                            }

            for key, value in types_allowed.iteritems():
                if _url.find(key) >= 0:
                    return value

            return ""
        except Exception, ex:
            print ex.message
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)