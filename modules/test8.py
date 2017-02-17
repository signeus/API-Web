from core.core import Core
from bson import ObjectId

from timeit import timeit

Core()
#result = core.PostOperation("like2Post", {'id':'58a3298c481f3406cf184ca2', 'id_user':'5891cced481f3416aa786783'})
#print result

pa = {
    "_id" : ObjectId("58a3298c481f3406cf184ca2"),
    "user_id" : "5891cced481f3416aa786783",
    "date_modified" : "2017-02-16T15:09:21.630Z",
    "community_id" : "5898addd481f344586a88673",
    "date_created" : "2017-02-14T16:00:12.719Z",
    "post" : "POPOPPOOPop",
    "likes" : [ 
        ObjectId("5891cd34481f3416aa786785"), 
        ObjectId("5891cced481f3416aa786783")
    ]
}

result = Core().InternalOperation("castDictObjectsId2DictHexIdRecursService", {"dictionary": pa})
print result
