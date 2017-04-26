# -*- coding: utf-8 -*-
import unicodedata
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from django.utils.encoding import smart_str,force_unicode,smart_bytes, smart_unicode

#parameters=list
class CastUrlEmailTextService(IService):
    def __init__(self, core,parameters):
        super(CastUrlEmailTextService, self).__init__(core, parameters)

    def run(self):
        listOrigin=self.parameters
        listWords=[]
        for i in listOrigin:
            if not("www") in i:
                if not("@") in i:
                    listWords = listWords + [i]
        return listWords