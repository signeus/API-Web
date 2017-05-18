# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def createUser():
    core = Core()
    result = core.UserOperation("createUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars,  "getFirstByFieldsUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getFirstByFieldsUser():
    core = Core()
    result = core.UserOperation("getFirstByFieldsUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars,  "getByIdUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getByIdUser():
    _id = request.vars["_id"]
    core = Core()
    result = core.UserOperation("getByIdUser", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getUsers():
    core = Core()
    result = core.UserOperation("getAllUser", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["DELETE"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, "deleteUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def deleteUser():
    _id = request.vars["_id"]
    core = Core()
    result = core.UserOperation("deleteUser", {"_id":_id})
    if result >= 1:
        return response.json({"result":"success"})
    return response.json({"result":"failed"})

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, "updateUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def updateUser():
    _id = request.vars["_id"]
    _new_values = request.vars["new_values"]
    core = Core()
    result = core.UserOperation("updateUser", {"_id":_id, "new_values":_new_values})
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, "subscribeUser2Community")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def subscribeUser2Community():
    core = Core()
    result = core.UserOperation("subscribeUser2Community", dict(request.vars))
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def unsubscribeUser2Community():
    core = Core()
    result = core.UserOperation("unsubscribeUser2Community", dict(request.vars))
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, "getUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getUser():
    _id = request.vars["id"]
    core = Core()
    result = core.UserOperation("getUserSubscribedCommunities", {"_id": _id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getAllUsersFiltered():
    core = Core()
    result = core.UserOperation("getAllUsersFiltered", dict(request.vars))
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, "loginUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def login():
    return response.json(Core().UserOperation("loginUser", dict(request.vars)))

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars,  "signup")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def signup():
    core = Core()
    result = core.UserOperation("signup", dict(request.vars))
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars,  "updateUserProfile")
def updateUserProfile():
    result = Core().UserOperation("updateUserProfile", dict(request.vars))
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def newUser():
    core = Core()
    result = core.UserOperation("newUser", request.vars)
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, "findUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findUserService():
    return response.json(Core().UserOperation("findUser", dict(request.vars)))

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars,  "subscribeUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def subscribeUser():
    return response.json(Core().UserOperation("subscribeUser", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, "changeUserLanguage")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def changeUserLanguage():
    return response.json(Core().UserOperation("changeUserLanguage", dict(request.vars)))