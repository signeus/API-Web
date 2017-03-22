# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import urllib

class CheckContentTypeUrlService (IService):
    def __init__(self, core, parameters):
        super(CheckContentTypeUrlService, self).__init__(core, parameters)

    def run(self):
        _url = self.parameters.get("link", None)
        validateUrl = self.core.InternalOperation("validateUrl", {'url': _url})

        if not validateUrl or "":
            raise Exception("The url is not valid.")

        embedUrl = self.core.InternalOperation("generateEmbedExternalUrl", {'link': _url})
        if embedUrl:
            return embedUrl

        res = urllib.urlopen(validateUrl)

        result = {}

        http_message = res.info()
        full = http_message.type  # 'text/plain'
        main_type = http_message.maintype  # 'text'

        result["mime"] = full
        result["type"] = main_type
        result["link"] = validateUrl

        return result