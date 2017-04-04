# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def createCommunity():
    core = Core()
    result = core.CommunityOperation("createCommunity", dict(request.vars))
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"_id":"optional"}, "getFirstByFieldsCommunity")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getFirstByFieldsCommunity():
    core = Core()
    result = core.CommunityOperation("getFirstByFieldsCommunity", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"_id":"mandatory"}, "getByIdCommunity")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getByIdCommunity():
    _id = request.vars["_id"]
    core = Core()
    result = core.CommunityOperation("getByIdCommunity", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getCommunities():
    core = Core()
    result = core.CommunityOperation("getAllCommunity", {})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["DELETE"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"_id":"mandatory"}, "deleteCommunity")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def deleteCommunity():
    _id = request.vars["_id"]
    core = Core()
    result = core.CommunityOperation("deleteCommunity", {"_id":_id})
    if result >= 1:
        return "Success"
    return "Failed"

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"_id":"mandatory", "new_values":"mandatory"}, "updateCommunity")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def updateCommunity():
    _id = request.vars["_id"]
    _new_values = request.vars["new_values"]
    core = Core()
    result = core.CommunityOperation("updateCommunity", {"_id":_id, "new_values":_new_values})
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def newCommunity():
    return response.json(Core().CommunityOperation("newCommunity", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"user_id":"mandatory"}, "getAllCommunities")
def getAllCommunities():
    return response.json(Core().CommunityOperation("getAllCommunities", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"user_id":"mandatory","start":"optional","offset":"optional"}, "getAllCommunities")
def getCommunitiesByUser():
    return response.json(Core().CommunityOperation("getCommunities", dict(request.vars)))

def countCommunityMembers():
    return response.json(Core().CommunityOperation("countCommunityMembers", dict(request.vars)))