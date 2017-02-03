# -*- coding: utf-8 -*-

from decorators.generic_decorator import GENERIC_DECORATOR
from http.http_exception import HttpException

class HTTP_METHOD_CONSTRAINT_DECORATOR:
    @staticmethod
    @GENERIC_DECORATOR.parametrized
    def isAllowed(f, methodsAllowed, request):
        def decorator(*args, **kwargs):
            allowsMethods = methodsAllowed
            if not request.env.request_method in allowsMethods:
                raise HttpException(405)
            return f(*args, **kwargs)

        return decorator
