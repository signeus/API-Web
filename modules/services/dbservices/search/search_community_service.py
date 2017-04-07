from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class SearchCommunityService(IService):
    def __init__(self, core, parameters):
        super(SearchCommunityService, self).__init__(core, parameters)

    def run(self):
        print "Encontrar Community"
        name=self.parameters["search"]
        print name
        found = DBService(self.core).getAllByFilter("Communities",
                                                  {"name": name})
        communityFound = {}
        communityFound["CommunityFound"] = found
        return communityFound
