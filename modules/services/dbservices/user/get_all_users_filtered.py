# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_object_id import CasterObjectId
from casters.caster_cursor import CasterCursor


class GetAllUsersFiltered(IService):
    def __init__(self, core, parameters):
        super(GetAllUsersFiltered, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters

    def run(self):
        result = DBService().getAllByFilter("Users", self.parameters.get('query', {}), self.parameters.get('filter',{}))
        result = CasterObjectId().castDictionaryObjectsId2DictionaryHexId(result)
        result = CasterCursor().castList2FormatDictionary(result)

        return result
