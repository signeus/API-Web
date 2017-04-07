from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class SearchAllService(IService):
    def __init__(self, core, parameters):
        super(SearchAllService, self).__init__(core, parameters)

    def run(self):
        print "Encontrar en todos"
        foundUser=self.core.InternalOperation("searchUserService", self.parameters)
        foundCommunity = self.core.InternalOperation("searchCommunityService", self.parameters)
        foundPost = self.core.InternalOperation("searchPostService", self.parameters)
        foundComment=self.core.InternalOperation("searchCommentService", self.parameters)

        allFound=[foundUser]
        allFound =allFound+[foundCommunity]
        allFound = allFound + [foundPost]
        allFound=allFound + [foundComment]
        print allFound
        return allFound
