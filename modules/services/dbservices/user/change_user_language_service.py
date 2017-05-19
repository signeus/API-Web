# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class ChangeUserLanguageService (IService):
    def __init__(self, core, parameters):
        super(ChangeUserLanguageService, self).__init__(core, parameters)

    def run(self):
        _lang = self.parameters.get("lang", "en")
        _user_id = self.parameters.get("id", "")
        user_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _user_id})
        language = "profile.language"
        info = self.core.InternalOperation("replaceInsideFieldsUser", {"id":user_ObjectId, "field_path":language, "value":_lang})

        if info.get("nModified", 0) == 1:
            return {"id": user_ObjectId, "lang":_lang}