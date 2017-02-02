# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT("GET", request)
@CROSS_DOMAIN(response)
def getFirstByFieldsPost():
    header(response)
    core = Core()
    result = core.PostOperation("getFirstByFieldsPost", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
@CROSS_DOMAIN(response)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"getByIdPost")
def getByIdPost():
    _id = request.vars["id"]
    header(response)
    core = Core()
    result = core.PostOperation("getByIdPost", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("GET", request)
@CROSS_DOMAIN(response)
def getPosts():
    core = Core()
    header(response)
    result = core.PostOperation("getAllPost", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("DELETE", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"deletePost")
@CROSS_DOMAIN(response)
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
@CROSS_DOMAIN(response)
def newPost():
    core = Core()
    result = core.PostOperation("createPost", dict(request.vars))
    return response.json(result)

@HTTP_METHOD_CONSTRAINT("POST", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory", "new_values":"mandatory"},"updatePost")
@CROSS_DOMAIN(response)
def updatePost():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    header(response)
    result = core.PostOperation("updatePost", {"_id":_id, "new_values":_new_values})
    return response.json(result)
