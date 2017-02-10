# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_object_id import CasterObjectId
from casters.caster_datetime import CasterDatetime
from casters.caster_cursor import CasterCursor


class GetPostsByCommunityId(IService):
    def __init__(self, core, parameters):
        super(GetPostsByCommunityId, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        result = DBService(self.core).getAllByFilter("Posts", self.parameters,  {'community_id':0})
        #TODO Extract Caster to Service
        result = CasterObjectId().castDictionaryObjectsId2DictionaryHexId(result)
        result = CasterDatetime().castDictionaryDateObject2DateTimeStamp(result)
        result = CasterCursor().castList2FormatDictionary(result)

        return result
