# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetPostService (IService):
    def __init__(self, core, parameters):
        super(GetPostService, self).__init__(core, parameters)

    def run(self):
        _post_id = self.parameters.get("post_id", "")

        if not _post_id:
            raise Exception("Get post: Empty post id not allowed.")

        post = self.core.InternalOperation("getPostById", {"id": _post_id})
        comments = self.core.InternalOperation("getCommentsPost", {"post_id": _post_id})
        post["comments"] = comments
        result = self.core.InternalOperation("castDict2FormatDict", {"dictionary":post})
        return result