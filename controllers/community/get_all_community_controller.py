# -*- coding: utf-8 -*-
import json
from core.core import Core

@HTTP_METHOD_CONSTRAINT("GET", request)
def getCommunities():
    core = Core()
    result = core.CommunityOperation("getAllCommunity", {})
    return response.json(result)
