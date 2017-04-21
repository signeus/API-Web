# -*- coding: utf-8 -*-
import pprint
from core.core import Core
from bson import ObjectId
from datetime import datetime
from timeit import timeit


Core()
#result = core.PostOperation("like2Post", {'id':'58a3298c481f3406cf184ca2', 'id_user':'5891cced481f3416aa786783'})
#print result

#result = Core().InternalOperation("castDictObjectsId2DictHexIdRecursService", {"iter": po})
#print result
#ids = "5898abfd481f3443d8917fce"
#result = Core().PostOperation("updatePost", {"_id":"58a6eddc481f3432c5534ad0", "new_values":{"post":str("Hey, esto ha sido modificado")}})
#print result

#http://192.168.1.176:8001/kayoo2/user/getUser?_id=5891cced481f3416aa786783
#http://192.168.1.176:8001/kayoo2/post/getCommunityPosts?id=5898abfd481f3443d8917fce


#result = Core().UserOperation("getUserSuscribedCommunities", {"_id":"5891cced481f3416aa786783"})
#print result

result = Core().CommunityOperation("newCommunity", {"description":"", "name": "Comunity test"})
#result = Core().SearchOperation("find", {"search":"co"})
#result = Core().SearchOperation("getCommunityInfo", {"community_id":"58e4fede481f34078ba6655c"})
#print dict(result)
#p=pprint.PrettyPrinter(indent=4)
#p.pprint(dict(result))

