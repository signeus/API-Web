# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"_id":"optional"}, "getFirstByFieldsUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getFirstByFieldsUser():
    core = Core()
    result = core.UserOperation("getFirstByFieldsUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"_id":"mandatory"}, "getByIdUser")
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
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"_id":"mandatory"}, "deleteUser")
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
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def newUser():
    core = Core()
    result = core.UserOperation("createUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
#@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory", "new_values":"mandatory"}, "updateUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def updateUser():
    print request.vars
    print request.client
    #_id = request.vars["_id"]
    #_new_values = request.vars["new_values"]
    #core = Core()
    #result = core.UserOperation("updateUser", {"_id":_id, "new_values":_new_values})
    #print result
    #return response.json(result)
    return "OK"

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id_user":"mandatory", "id_community":"mandatory"}, "suscribeUser2Community")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def suscribeUser2Community():
    core = Core()
    result = core.UserOperation("suscribeUser2Community", dict(request.vars))
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def unsuscribeUser2Community():
    core = Core()
    result = core.UserOperation("unsuscribeUser2Community", dict(request.vars))
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getUser():
    _id = request.vars["id"]
    core = Core()
    result = core.UserOperation("getUserSuscribedCommunities", {"_id": _id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getAllUsersFiltered():
    core = Core()
    result = core.UserOperation("getAllUsersFiltered", dict(request.vars))
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"mail":"mandatory", "psswd":"mandatory"}, "loginUser")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def login():
    core = Core()
    result = core.UserOperation("loginUser", dict(request.vars))
    return response.json(result)