# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class Comment2PostService (IService):
    def __init__(self, core, parameters):
        super(Comment2PostService, self).__init__(core, parameters)

    def run(self):
        try:
            _post_id = self.parameters.get("post_id", None)
            files = self.parameters.pop("files",{})

            checkedUrls = self.core.InternalOperation("checkPostUrls",
                                                      {"files": files})

            files = checkedUrls.pop("filesAttachment", {})

            print checkedUrls

            self.parameters = dict(self.parameters, **checkedUrls)

            if _post_id:
                self.parameters["post_id"] = self.core.InternalOperation("castHex2ObjectId", {"id":_post_id})

            result = self.core.InternalOperation("createPost", self.parameters)

            # TODO New service "POST Attachment"
            if files:
                filesRoutes = self.core.InternalOperation("savePostFiles", {'id': result['_id'], 'files': files})
                return dict(result, **{'files':filesRoutes})

            return result
        except Exception, ex:
            print ex.message
