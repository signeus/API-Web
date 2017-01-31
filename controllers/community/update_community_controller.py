# -*- coding: utf-8 -*-
import json
from core.core import Core

@HTTP_METHOD_CONSTRAINT("POST", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory", "new_values":"mandatory"},"updateCommunity")
def updateCommunity():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    result = core.CommunityOperation("updateCommunity", {"_id":_id, "new_values":_new_values})
    return response.json(result)
