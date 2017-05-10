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

#result = Core().CommunityOperation("newCommunity",
#									{"description":"prueba para crear community con OPS ", "name": "optionals",
#									 "administrators[0]": "5891cc74481f3416aa78677c", "leaders": "Lucia" ,
#									 "creator_id":"5891cc74481f3416aa78677c", "environement_type":"0", "community_type": "0",} )
#result = Core().SearchOperation("getCommunityInfo", {"community_id":"58e4fede481f34078ba6655c"})

#result = Core().InternalOperation("getRandomPostComment", "")
#result = Core().InternalOperation("castReplaceText", "Este. texto, de prueba: tenia! muchas? cosas... incluso www.loquesea.com y tambien un@email.es y las cosas con tildes no sé no sé")
#result = Core().InternalOperation("castSeparateText", "Este. texto, de prueba: tenia! muchas? cosas... incluso www.loquesea.com y tambien un@email.es")
#resul=Core().InternalOperation("castDiacritics2Normalize", "quiero quitar las tildes de no sé no sé")
result = Core().InternalOperation("getCommunityPosts", {"community_id":"58f61094481f343de6d5dc17", "user_id":"5891cced481f3416aa786783"})

#result = Core().InternalOperation("newSurveyAnswer", {"post_id":"58e209db481f340e18c0beb4", "user_id":"5891cc74481f3416aa78677c", "answer_id":"0"})
#result=Core().CommunityOperation("getAllCommunities", {"user_id":"5891cd89481f3416aa786789"})
#print dict(result)
#p=pprint.PrettyPrinter(indent=4)
#p.pprint(dict(result)) 

#, "leaders": ["Lucia"]
#5891cc74481f3416aa78677c

#"Este post es para ver como hago para separar las palabras, omito las comas. Tambien los puntos... y si son puntos suspensivos o si hay una arroba como aqui: mi@correo.com o si hay una web como www.loquesea.es y los http y las interrogaciones? o exclamaciones! y las cosas con tildes no sé no sé"
