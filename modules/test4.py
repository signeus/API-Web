#from core.core import Core
from decorators.http_method_constraint import HTTP_METHOD_CONSTRAINT

#core = Core()
#print core.CommunityOperation("getAllCommunity", {})
#print core.CommunityOperation("createCommunity", {"name":"Cat", "valores":"Muy mono"})
#print core.CommunityOperation("updateCommunity", {"_id":"588f19d8481f341953b11159", "new_values":{"name":"Amelio", "valores":"Muy perro"}})
#print core.CommunityOperation("deleteCommunity", {"_id":"588f1634481f3417718a4cb7"})
#print core.CommunityOperation("getByIdCommunity", {"_id":"588f19d8481f341953b11159"})
#print core.CommunityOperation("getFirstByFieldsCommunity", {"fields":{"name":"Cat"}})

#print core.UserOperation("createUser", {})
#print core.UserOperation("getAllUser", {})

#print core.UserOperation("createPost", {"user":"Pepe","comment":"Hey!"})
#print core.PostOperation("getAllPost",{})

#from services.dbservices.community.create_community_service import CreateCommunityService
#c = CreateCommunityService()


#core = Core()
#

@HTTP_METHOD_CONSTRAINT(["POST","OPTIONS"],)
def uiu():
    print "vvv"
    
    
    
uiu()
    
