# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import re

class ValidateUrlService (IService):
    def __init__(self, core, parameters):
        super(ValidateUrlService, self).__init__(core, parameters)

    def run(self):
        url = self.parameters.get("url", None)
        if not url:
            return None

        urlVideo = re.findall(str('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
                              str(url))
        if len(urlVideo) == 0:
            return None

        validate = URLValidator()
        try:
            validate(urlVideo[0])
            if self.core.InternalOperation("existsUrl", {'url': urlVideo[0]}):
                return urlVideo[0]
        except ValidationError, e:
            return ""

        return ""
