from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class SearchUserService(IService):
    def __init__(self, core, parameters):
        super(SearchUserService, self).__init__(core, parameters)

    def run(self):
        print "Encontrar User"
        name=self.parameters["search"]
        print name
        found = DBService(self.core).getAllByFilter("Users",
                                                  {"name": name})
        usersFound = {}
        usersFound["UsersFound"] = found
        return usersFound
