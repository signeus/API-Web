# -*- coding: utf-8 -*-
import json
from core.core import Core

@HTTP_METHOD_CONSTRAINT("GET", request)
def getFirstByFieldsUser():
    core = Core()
    result = core.UserOperation("getFirstByFieldsUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"getByIdUser")
def getByIdUser():
    _id = request.vars["id"]
    core = Core()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    response.headers['Access-Control-Allow-Headers']= "origin, content-type, accept"
    response.headers['Access-Control-Allow-Methods']= "GET, POST, OPTIONS, DELETE"
    result = core.UserOperation("getByIdUser", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
def getUsers():
    core = Core()
    result = core.UserOperation("getAllUser", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("DELETE", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"deleteUser")
def deleteUser():
    _id = request.vars["id"]
    core = Core()
    result = core.UserOperation("deleteUser", {"_id":_id})
    if result >= 1:
        return "Success"
    return "Failed"

@HTTP_METHOD_CONSTRAINT("POST", request)
def newUser():
    core = Core()
    result = core.UserOperation("createUser", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("POST", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory", "new_values":"mandatory"},"updateUser")
def updateUser():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    result = core.UserOperation("updateUser", {"_id":_id, "new_values":_new_values})
    return response.json(result)

def suscribeUser2Community():
    return "Suscrito"