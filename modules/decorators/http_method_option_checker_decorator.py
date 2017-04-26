# -*- coding: utf-8 -*-

from decorators.generic_decorator import GENERIC_DECORATOR

class HTTP_METHOD_OPTION_CHECKER_DECORATOR:
    @staticmethod
    @GENERIC_DECORATOR.parametrized
    def isOption(f, request, response):
        def decorator(*args, **kwargs):
            if request.env.request_method == 'OPTIONS':
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Credentials'] = True
                response.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept"
                response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, DELETE"
                return response.json({"Options": "ALLOWED"})
            return f(*args, **kwargs)

        return decorator
