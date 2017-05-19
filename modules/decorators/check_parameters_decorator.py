# -*- coding: utf-8 -*-
from k_exception.check_exception            import CheckException
from decorators.generic_decorator           import GENERIC_DECORATOR
from controllers.controller_params_factory  import ControllerParamsFactory

class CHECK_PARAMETERS_DECORATOR:
    @staticmethod
    @GENERIC_DECORATOR.parametrized

    def checkIt(f, reqVars, method):
        def decorator(*args, **kwargs):

            ### Empty parameters ###
            if len(reqVars) <= 0:

                try:
                    raise CheckException(method, {}, "EMPTY")
                except Exception as ex:
                    return ex
            params=ControllerParamsFactory().getParams(method)
            ### Mandatory Condition ###
            parameterMandatory = False

            for k, v in params.iteritems():

                if (v == "mandatory" ):
                    if not k in reqVars:
                        parameterMandatory = True
                        break
                if k=="administrators":
                    for key, value in reqVars.iteritems():
                        if key=="administrators":
                            if "," in value:
                                val=value.split(",")
                                reqVars["administrators"]=val
                                break
                            else:
                                reqVars["administrators"] = value

                                break

            if parameterMandatory:
                try:
                    raise CheckException(method, {k: v}, "MANDATORY")
                except Exception as ex:
                    return ex
            ### Too parameters ###
            cKsParams = set(params.keys())
            cKsReqVars = set(reqVars.keys())
            leftElems = cKsReqVars - cKsParams
            optionalParams = []
            for k, v in params.iteritems():
                if v == "optional":
                    optionalParams.append(k)

            excessParams = {}
            for elem in leftElems:
                if not elem in optionalParams:
                    excessParams.update({elem: "EXCESS"})
            if len(excessParams) > 0:
                try:
                    raise CheckException(method, excessParams, "TOO_PARAMETERS")
                except Exception as ex:
                    return ex
            return f(*args, **kwargs)


        return decorator
