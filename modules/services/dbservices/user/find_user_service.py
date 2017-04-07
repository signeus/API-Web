from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class FindUserService(IService):
    def __init__(self, core, parameters):
        super(FindUserService, self).__init__(core, parameters)

    def run(self):
        print "hola"
        name=self.parameters["name"]
        print name
        found = DBService(self.core).getAllByFilter("Users",
                                                  {"name": name})
        print found
        usersFound = {}
        usersFound["UsersFound"] = found
        print usersFound
        return usersFound
