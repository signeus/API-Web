# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_cursor import CasterCursor


class GetAllUsersFiltered(IService):
    def __init__(self, core, parameters):
        super(GetAllUsersFiltered, self).__init__(core, parameters)

    def run(self):
        result = DBService(self.core).getAllByFilter("Users", self.parameters.get('query', {}), self.parameters.get('filter',{}))
        result = CasterCursor().castList2FormatDictionary(result)

        for elems in result:
            result[elems]["avatar"] = self.core.InternalOperation("getMediaRoute", {"service":"getAvatarById", "attribs":{"id":str(elems)}})

        return result
        #result = [dict(elem,**{'avatar': self.core.InternalOperation("getMediaRoute", {"service":"getAvatarById", "attribs":{"id":str(elem)}})}) for elem in result]