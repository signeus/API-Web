from core.core import Core
from bson import ObjectId
from timeit import timeit

core = Core()
#result = core.MediaOperation("getAvatarById", {"_id": "5891cd34481f3416aa786785"})
#print result
#Core().CommunityOperation("getByIdCommunity", {"_id":"588f1912481f341939ca31fd"})
#Core().CommunityOperation("getCommunityPosts", {"community_id":"589dc215481f34550e335f90"})
#result = Core().PostOperation("updatePost", {"_id":'589dc215481f34550e335f90', "new_values":{"post":str("Editando")}})
po = [ObjectId('5891cced481f3416aa786783'), ObjectId('5891cced481f3416aa786783'), ObjectId('5891cced481f3416aa786783'), ObjectId('5891cced481f3416aa786783'), ObjectId('5891cced481f3416aa786783'), ObjectId('5891cced481f3416aa786783')]

#result = core.PostOperation("like2Post", {'id':'58a3298c481f3406cf184ca2', 'id_user':'5891cced481f3416aa786783'})

def ll():
	return core.InternalOperation("castListObjectsId2ListHexId", {"lis": po})

#print timeit(metodo4,number = 1) 
for l in xrange(0,1000):
	print timeit(ll, number=1) * 1000  

# result1 = 0.0219345092773
# result2 = 0.032901763916

