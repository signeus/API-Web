# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getFirstByFieldsPost():
    header(response)
    core = Core()
    result = core.PostOperation("getFirstByFieldsPost", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getByIdPost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getByIdPost():
    _id = request.vars["id"]
    header(response)
    core = Core()
    result = core.PostOperation("getByIdPost", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getPosts():
    core = Core()
    header(response)
    result = core.PostOperation("getAllPost", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["DELETE"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "deletePost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def deletePost():
    _id = request.vars["id"]
    core = Core()
    header(response)
    result = core.PostOperation("deletePost", {"_id":_id})
    if result >= 1:
        return "Success"
    return "Failed"

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def newPost():
    core = Core()
    result = core.PostOperation("createPost", dict(request.vars))
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory", "new_values":"mandatory"}, "updatePost")
def updatePost():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    header(response)
    result = core.PostOperation("updatePost", {"_id":_id, "new_values":_new_values})
    return response.json(result)
