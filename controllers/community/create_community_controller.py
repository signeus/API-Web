# -*- coding: utf-8 -*-
from core.core import Core

@HTTP_METHOD_CONSTRAINT("POST", request)
def newCommunity():
    core = Core()
    result = core.CommunityOperation("createCommunity", request.vars)
    return result
