# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_cursor import CasterCursor


class GetCommentsByPostId(IService):
    def __init__(self, core, parameters):
        super(GetCommentsByPostId, self).__init__(core, parameters)

    def run(self):
        result = DBService(self.core).getAllByFilter("Posts", self.parameters,  {'post_id':0})
        result = CasterCursor().castList2FormatDictionary(result)
        return result
