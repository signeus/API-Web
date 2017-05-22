# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class UnsubscribeUser2Community (IService):
    def __init__(self, core, parameters):
        super(UnsubscribeUser2Community, self).__init__(core, parameters)

    def run(self):
        # Retrieve the data about user and community.
        _community = self.parameters.get("community", {})
        _user = self.parameters.get("user", {})

        result = self.core.InternalOperation("extractInsideFieldsUser",
                                                   {"id": _user["_id"], "field_path": "communities_subscribed",
                                                    "value": _community["_id"]})
        #Correct and modify, return only the ID
        if result.get("nModified", 0) == 1:
            return {"id": _community["_id"]}
