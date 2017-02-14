from core.core import Core

#core = Core()
#result = core.MediaOperation("getAvatarById", {"_id": "5891cd34481f3416aa786785"})
#print result
#Core().CommunityOperation("getByIdCommunity", {"_id":"588f1912481f341939ca31fd"})
#Core().CommunityOperation("getCommunityPosts", {"community_id":"589dc215481f34550e335f90"})
result = Core().PostOperation("updatePost", {"_id":'589dc215481f34550e335f90', "new_values":{"post":str("Editando")}})
