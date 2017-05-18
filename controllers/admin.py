@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars,  "adminManageSubscriptions")
def AdminManageSubscriptions():

    return response.json(Core().AdminOperation("adminManageSubscriptions", dict(request.vars)))

