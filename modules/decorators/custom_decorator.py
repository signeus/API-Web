class CUSTOM_DECORATOR(object):
    @staticmethod
    @GENERIC_DECORATOR.parametrized
    def loquesea(f, n, m):
        def decorator(*args, **kwargs):
            print n
            print m
            return f(*args, **kwargs)

        return decorator
