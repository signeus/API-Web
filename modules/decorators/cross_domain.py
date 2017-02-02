# -*- coding: utf-8 -*-
class CROSS_DOMAIN:
    def __init__(self, response):
        self.response = response

    def __call__(self, function):
        def wrapped_func():
            self.response.headers['Access-Control-Allow-Origin'] = '*'
            self.response.headers['Access-Control-Allow-Credentials'] = True
            self.response.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept"
            self.response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, DELETE"
            return function()

        return wrapped_func
