# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT("GET", request)
@CROSS_DOMAIN(response)
def getFirstByFieldsUser():
    core = Core()
    result = core.UserOperation("getFirstByFieldsUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"getByIdUser")
@CROSS_DOMAIN(response)
def getByIdUser():
    _id = request.vars["id"]
    core = Core()
    result = core.UserOperation("getByIdUser", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
@CROSS_DOMAIN(response)
def getUsers():
    core = Core()
    result = core.UserOperation("getAllUser", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("DELETE", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"deleteUser")
@CROSS_DOMAIN(response)
def deleteUser():
    _id = request.vars["id"]
    core = Core()
    result = core.UserOperation("deleteUser", {"_id":_id})
    if result >= 1:
        return "Success"
    return "Failed"

@HTTP_METHOD_CONSTRAINT("POST", request)
@CROSS_DOMAIN(response)
def newUser():
    core = Core()
    result = core.UserOperation("createUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("POST", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory", "new_values":"mandatory"},"updateUser")
@CROSS_DOMAIN(response)
def updateUser():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    result = core.UserOperation("updateUser", {"_id":_id, "new_values":_new_values})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("POST", request)
@CROSS_DOMAIN(response)
def suscribeUser2Community():
    core = Core()
    result = core.UserOperation("suscribeUser2Community", dict(request.vars))
    return "Suscrito"