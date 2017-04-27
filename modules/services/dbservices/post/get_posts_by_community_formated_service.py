# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from casters.caster_cursor import CasterCursor


class GetPostsByCommunityFormatedService(IService):
    def __init__(self, core, parameters):
        super(GetPostsByCommunityFormatedService, self).__init__(core, parameters)

    def run(self):
        _id = self.parameters.get("community_id", 0)
        _ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _id})
        result = self.core.InternalOperation("getPostsByCommunityId", {"community_id":_ObjectId})
        #TODO Adapt this with Core.InternalOperation

        result = CasterCursor().castList2FormatDictionary(result)

        return result
