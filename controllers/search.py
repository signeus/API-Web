# -*- coding: utf-8 -*-

#@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
#@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
#@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
#def search():
#   return response.json({"data":[{"search":"Tomate"},
#     {"search": "Arroz"},
#     {"search": "Berenjena"}], "result":0})

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"search":"mandatory"}, "searchUserService")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findUserService():
    return response.json(Core().SearchOperation("searchUserService", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"search":"mandatory"}, "searchPostService")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findPostService():
    return response.json(Core().SearchOperation("searchPostService", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"search":"mandatory"}, "searchCommunityService")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findCommunityService():
    return response.json(Core().SearchOperation("searchCommunityService", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"search":"mandatory"}, "searchCommentService")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findCommentService():
    return response.json(Core().SearchOperation("searchCommentService", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"search":"mandatory"}, "searchAllService")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findAllService():
    return response.json(Core().SearchOperation("searchAllService", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"search":"mandatory"}, "find")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findUser():
    return response.json(Core().SearchOperation("findUser", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"search":"mandatory"}, "find")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def find():
    return response.json(Core().SearchOperation("find", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def findDic():
    return response.json({"a":1, "b":2, "c":3})
