class GENERIC_DECORATOR:

    @staticmethod
    def parametrized(dec):
        def decorator(*args,**kwargs):
            def wrapped_func(f):
                return dec(f,*args,**kwargs)
            return wrapped_func
        return decorator