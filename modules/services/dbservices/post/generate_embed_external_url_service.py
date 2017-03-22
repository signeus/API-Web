# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import sys, os

class GenerateEmbedExternalUrlService (IService):
    def __init__(self, core, parameters):
        super(GenerateEmbedExternalUrlService, self).__init__(core, parameters)

    def run(self):
        _url = self.parameters.get("link", None)
        try:
            type = self.core.InternalOperation("identifyExternalUrl", {'link': _url})
            if not type:
                return ""

            streaming_type = ['twitch','gaming.youtube']
            types = {
                        'youtube' : 'https://www.youtube.com/embed/'+ type.get("id","") +'?',
                        'twitch.tv/videos' : 'http://player.twitch.tv/?video=v'+ type.get("id","") +'&',
                        'twitch' : 'http://player.twitch.tv/?channel='+ type.get("id",""),
                        'vimeo' : 'https://player.vimeo.com/video/'+ type.get("id","") +'?portrait=0&',
                        'gaming.youtube': 'https://gaming.youtube.com/embed/' + type.get("id", "") + '?'
                    }
            utils = {
                        'autoplay' : 'autoplay=1'
                    }

            embedUrl = types.get(type.get("name",''),"")
            if embedUrl:
                result = {}
                result["type"] = 'video'
                result["origin"] = 'url/' + type.get("name",'')
                print type.get("name",'')
                if not type.get("name",'') in streaming_type:
                    embedUrl = embedUrl + utils['autoplay']
                result["link"] = embedUrl
                return result

            return embedUrl
        except Exception, ex:
            print ex.message
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)