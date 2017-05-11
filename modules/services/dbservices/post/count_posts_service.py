from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class CountPostsService(IService):
    def __init__(self, core, parameters):
        super(CountPostsService, self).__init__(core, parameters)


    def run(self):
        _query = self.parameters.get("query",{})
        return DBService(self.core).countFields("Posts", _query)
