# -*- coding: utf-8 -*-
class InvalidFieldsException(Exception):
    def __init__(self, fields):
        self.fields = fields

    @property
    def message(self):
        return {"message": "Exception: Invalid fields", "fields":self.fields}

    def __str__(self):
        print self.message
        return self.message