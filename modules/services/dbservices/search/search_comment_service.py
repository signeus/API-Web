from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class SearchCommentService(IService):
    def __init__(self, core, parameters):
        super(SearchCommentService, self).__init__(core, parameters)

    def run(self):
        print "Encontrar comment"
        post=self.parameters["search"]
        print post
        found = DBService(self.core).getAllByFilter("Posts",
                                                  {"comment": post})
        commentFound = {}
        commentFound["commentFound"] = found
        return commentFound
