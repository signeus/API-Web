# -*- coding: utf-8 -*-
import json
from core.core import Core

@HTTP_METHOD_CONSTRAINT("GET", request)
#@CHECK_PARAMETERS(request.vars,{"id":"optional"},"getFirstByFieldsCommunity")
def getFirstByFieldsCommunity():
    core = Core()
    result = core.CommunityOperation("getFirstByFieldsCommunity", request.vars)
    return response.json(result)
