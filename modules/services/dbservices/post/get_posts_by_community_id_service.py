# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_cursor import CasterCursor


class GetPostsByCommunityId(IService):
    def __init__(self, core, parameters):
        super(GetPostsByCommunityId, self).__init__(core, parameters)

    def run(self):
        result = DBService(self.core).getAllByFilter("Posts", self.parameters,  {'community_id':0})
        #TODO Checking if works the "JSON" encoder
        #result = self.core.InternalOperation("castDictObjectsId2DictHexIdRecursService", {"iter": result})
        result = CasterCursor().castList2FormatDictionary(result)

        return result
