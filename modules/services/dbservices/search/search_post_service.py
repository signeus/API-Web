from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class SearchPostService(IService):
    def __init__(self, core, parameters):
        super(SearchPostService, self).__init__(core, parameters)

    def run(self):
        post=self.parameters["search"]
        found = DBService(self.core).getAllByFilter("Posts",
                                                  {"post": post})
        postFound = {}
        postFound["PostFound"] = found
        return postFound
