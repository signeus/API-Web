# -*- coding: utf-8 -*-
import json
from core.core import Core

@HTTP_METHOD_CONSTRAINT("GET", request)
#@CHECK_PARAMETERS(request.vars,{"id":"optional"},"getFirstByFieldsCommunity")
def getFirstByFieldsCommunity():
    core = Core()
    result = core.CommunityOperation("getFirstByFieldsCommunity", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"getByIdCommunity")
def getByIdCommunity():
    _id = request.vars["id"]
    core = Core()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    response.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept"
    response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, DELETE"
    result = core.CommunityOperation("getByIdCommunity", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
def getCommunities():
    core = Core()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    response.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept"
    response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, DELETE"
    result = core.CommunityOperation("getAllCommunity", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("DELETE", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"deleteCommunity")
def deleteCommunity():
    _id = request.vars["id"]
    core = Core()
    result = core.CommunityOperation("deleteCommunity", {"_id":_id})
    if result >= 1:
        return "Success"
    return "Failed"

@HTTP_METHOD_CONSTRAINT("POST", request)
def newCommunity():
    core = Core()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    response.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept"
    response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, DELETE"
    result = core.CommunityOperation("createCommunity", dict(request.vars))
    return result

@HTTP_METHOD_CONSTRAINT("POST", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory", "new_values":"mandatory"},"updateCommunity")
def updateCommunity():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    result = core.CommunityOperation("updateCommunity", {"_id":_id, "new_values":_new_values})
    return response.json(result)
