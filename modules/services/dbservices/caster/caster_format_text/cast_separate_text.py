# -*- coding: utf-8 -*-
import unicodedata
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from django.utils.encoding import smart_str,force_unicode,smart_bytes, smart_unicode


class CastSeparateTextService(IService):
    def __init__(self, core,parameters):
        super(CastSeparateTextService, self).__init__(core, parameters)

    def run(self):
        return self.parameters.split()
