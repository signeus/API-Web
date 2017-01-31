# -*- coding: utf-8 -*-
from core.core import Core

@HTTP_METHOD_CONSTRAINT("DELETE", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"deleteCommunity")
def deleteCommunity():
    _id = request.vars["id"]
    core = Core()
    result = core.CommunityOperation("getByIdCommunity", {"_id":_id})
    if result >= 1:
        return "Sucess"
    return "Failed"
