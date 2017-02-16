from core.core import Core
from bson import ObjectId
from timeit import timeit

core = Core()
result = core.PostOperation("like2Post", {'id':'58a3298c481f3406cf184ca2', 'id_user':'5891cced481f3416aa786783'})
print result
