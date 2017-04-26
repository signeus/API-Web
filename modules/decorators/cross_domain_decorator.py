# -*- coding: utf-8 -*-

from decorators.generic_decorator import GENERIC_DECORATOR

class CROSS_DOMAIN_DECORATOR:
    @staticmethod
    @GENERIC_DECORATOR.parametrized
    def changesHeaders(f, response):
        def decorator(*args, **kwargs):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Credentials'] = True
            response.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept"
            response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, DELETE"
            return f(*args, **kwargs)

        return decorator
