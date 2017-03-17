# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_cursor import CasterCursor


class GetCommentsByPostId(IService):
    def __init__(self, core, parameters):
        super(GetCommentsByPostId, self).__init__(core, parameters)

    def run(self):
        _post_id = self.parameters.get("post_id", None)
        self.parameters["post_id"] = self.core.InternalOperation("castHex2ObjectId", {"id": _post_id})
        result = DBService(self.core).getAllByFilter("Posts", self.parameters,  {'post_id':0})
        return result
