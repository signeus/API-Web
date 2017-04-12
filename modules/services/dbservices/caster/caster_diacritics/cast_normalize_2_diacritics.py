# -*- coding: utf-8 -*-
import unicodedata
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from django.utils.encoding import smart_str,force_unicode,smart_bytes, smart_unicode


class CastNormalize2DiacriticsService(IService):
    def __init__(self, core,parameters):
        super(CastNormalize2DiacriticsService, self).__init__(core, parameters)

    def run(self):
        value=smart_unicode(self.parameters.get("text", " "))

        DIACRITICS_REPLACEMENTS = {

            'a'     :   'àáâãäåāaÀÁÂÃÄÅĀA',
            'ae'    :   'æäÆÄ',
            'e'     :   'èéêëẽėęeÈÉÊËẼĘE',
            'i'     :   'ìíîïĩīįiÌÍÎÏĨĮI',
            'ie'    :   'ïÏ',
            'o'     :   'ðòóôõöøōoÒÓÔÕÖØŌO',
            'oe'    :   'œöÖŒ',
            'u'     :   'ùúûüµūuÙÚÛÜŪU',
            'ue'    :   'üÜ',
            'c'     :   'çćčcÇĆČC',
            'n'     :   'ñńnÑŃN',
            's'     :   'ßšśsŠŚS',
            'y'     :   'ýÿ¥yÝŸY',
            'z'     :   'žźżzŽŹŻZ'
        }

        newValue = ""
        for i in value:
            found = False
            for k,v in DIACRITICS_REPLACEMENTS.items():
                if smart_unicode(i) in smart_unicode(v):
                    newValue = newValue + "[" + smart_unicode(v) + "]"
                    found = True
                    break
            if not found:
                newValue = newValue + smart_unicode(i)

        return newValue