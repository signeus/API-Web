# -*- coding: utf-8 -*-
import json
from core.core import Core

@HTTP_METHOD_CONSTRAINT("GET", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"getByIdCommunity")
def getByIdCommunity():
    _id = request.vars["id"]
    core = Core()
    result = core.CommunityOperation("getByIdCommunity", {"_id":_id})
    return response.json(result)
