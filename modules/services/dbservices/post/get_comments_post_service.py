# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_object_id import CasterObjectId
from casters.caster_datetime import CasterDatetime
from casters.caster_cursor import CasterCursor


class GetCommentsPost(IService):
    def __init__(self, core, parameters):
        super(GetCommentsPost, self).__init__(core, parameters)

    def run(self):
        postId = self.parameters.get("post_id","")
        if postId == "":
            raise Exception("Get comments post: Empty post ID is not allowed.")
        comments = self.core.InternalOperation("getCommentsByPostId", {"post_id": postId})
        users = self.core.InternalOperation("getAllUsersFiltered", {'query': {}, 'filter': {'name': 1, 'nick': 1}})
        for comment in comments:
            _comment_object_id = self.core.InternalOperation("castObjectId2Hex", {"id": comment.get("_id", "")})
            files = self.core.InternalOperation("getPostFiles", {"id": _comment_object_id})
            if files:
               comment["files"] = files

            likes = comment.pop("likes", [])
            for like in likes:
                comment["likes"] = {}
                comment["likes"][str(like)]  = {'name': users[str(like)].get("name", ""), 'nick': users[str(like)].get("nick", "")}

        co = [dict(c,**users[str(c["user_id"])]) for c in comments]
        return co
