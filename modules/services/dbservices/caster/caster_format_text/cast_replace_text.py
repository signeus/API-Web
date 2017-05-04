# -*- coding: utf-8 -*-
import unicodedata
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from django.utils.encoding import smart_str,force_unicode,smart_bytes, smart_unicode

#parameters=list
class CastReplaceTextService(IService):
    def __init__(self, core,parameters):
        super(CastReplaceTextService, self).__init__(core, parameters)


    def run(self):
        PUNCTUATION_REPLACEMENTS = [

            ';',
            ',',
            '.',
            ':',
            '!',
            '?'
        ]

        value=self.parameters
        newValue=[]
        for elem in value:
            found=False
            for i in PUNCTUATION_REPLACEMENTS:
                if i in elem:
                    newValue= newValue + [elem.replace(i,"")]
                    found=True
            if not found:
                newValue=newValue +[elem]

        return newValue


