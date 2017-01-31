# -*- coding: utf-8 -*-
import json
from core.core import Core
from decorators.http_method_constraint import HTTP_METHOD_CONSTRAINT
from decorators.http_method_not_allowed_constraint import HTTP_METHOD_NOT_ALLOWED_CONSTRAINT

def met():
   response.headers['Access-Control-Allow-Origin'] = '*'
   response.headers['Access-Control-Allow-Credentials'] = True
   response.headers['Access-Control-Allow-Headers']= "origin, content-type, accept"
   response.headers['Access-Control-Allow-Methods']= "GET, POST, OPTIONS, DELETE"
   print "pipi"
   return "caca"

def header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    response.headers['Access-Control-Allow-Headers']= "origin, content-type, accept"
    response.headers['Access-Control-Allow-Methods']= "GET, POST, OPTIONS, DELETE"
    return response

@HTTP_METHOD_CONSTRAINT("GET", request)
def getFirstByFieldsPost():
    header(response)
    core = Core()
    result = core.PostOperation("getFirstByFieldsPost", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"getByIdPost")
def getByIdPost():
    _id = request.vars["id"]
    header(response)
    core = Core()
    result = core.PostOperation("getByIdPost", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
def getPosts():
    core = Core()
    header(response)
    result = core.PostOperation("getAllPost", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("DELETE", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"deletePost")
def deletePost():
    _id = request.vars["id"]
    core = Core()
    header(response)
    result = core.PostOperation("deletePost", {"_id":_id})
    if result >= 1:
        return "Success"
    return "Failed"

@HTTP_METHOD_CONSTRAINT(["POST", "OPTIONS"], request)
@HTTP_METHOD_NOT_ALLOWED_CONSTRAINT(request, response)
def newPost():
    core = Core()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    response.headers['Access-Control-Allow-Headers']= "origin, content-type, accept"
    response.headers['Access-Control-Allow-Methods']= "GET, POST, OPTIONS, DELETE"
    result = core.PostOperation("createPost", dict(request.vars))
    return json.dumps(result)

@HTTP_METHOD_CONSTRAINT("POST", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory", "new_values":"mandatory"},"updatePost")
def updatePost():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    header(response)
    result = core.PostOperation("updatePost", {"_id":_id, "new_values":_new_values})
    return response.json(result)
