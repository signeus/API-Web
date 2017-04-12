from bson import ObjectId
from core.core import Core


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

po = [
		 {u'date_created': '2017, 2, 7, 17, 48, 32, 370000)', u'post': u'', u'_id': ObjectId('589a0870481f3425f395c8a7'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 7, 17, 48, 32, 370000'}, 
		 {u'date_created': '2017, 2, 7, 17, 48, 32, 377000)', u'post': u'gkjjfgdgkljdf', u'_id': ObjectId('589a0870481f3425f395c8a9'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 7, 17, 48, 32, 377000'}, 
		 {u'date_created': '2017, 2, 7, 17, 48, 50, 790000)', u'post': u'vcvccvcv', u'_id': ObjectId('589a0882481f3425f395c8b1'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 7, 17, 48, 50, 790000'}, 
		 {u'date_created': '2017, 2, 7, 17, 53, 29, 500000)', u'post': u'', u'_id': ObjectId('589a0999481f3425f395c8b3'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 7, 17, 53, 29, 500000'}, 
		 {u'date_created': '2017, 2, 7, 17, 53, 29, 514000)', u'post': u'dgsdgsd', u'_id': ObjectId('589a0999481f3425f395c8b5'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 7, 17, 53, 29, 514000'}, 
		 {u'date_created': '2017, 2, 7, 17, 53, 31, 965000)', u'post': u'', u'_id': ObjectId('589a099b481f3425f395c8b7'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 7, 17, 53, 31, 965000'}, 
		 {u'date_created': '2017, 2, 7, 17, 53, 31, 984000)', u'post': u'ssdsd', u'_id': ObjectId('589a099b481f3425f395c8b9'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 7, 17, 53, 31, 984000'}, 
		 {u'date_created': '2017, 2, 8, 10, 29, 22, 673000)', u'post': u'saasas', u'_id': ObjectId('589af302481f3406fa367bb0'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 8, 10, 29, 22, 673000'}, 
		 {u'date_created': '2017, 2, 8, 10, 29, 25, 631000)', u'post': u'asassa', u'_id': ObjectId('589af305481f3406fa367bb2'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 8, 10, 29, 25, 631000'}, 
		 {u'date_created': '2017, 2, 8, 10, 29, 29, 620000)', u'post': u'dfsdfdsf', u'_id': ObjectId('589af309481f3406fa367bb4'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 8, 10, 29, 29, 620000'}, 
		 {u'date_created': '2017, 2, 10, 13, 37, 37, 834000)', u'post': u'Popopopopopo', u'_id': ObjectId('589dc221481f34550e335f94'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 10, 13, 37, 37, 834000'}, 
		 {u'date_created': '2017, 2, 14, 11, 39, 18, 222000)', u'post': u'fffff', u'_id': ObjectId('58a2ec66481f34192cb33d70'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 14, 11, 39, 18, 222000'}, 
		 {u'date_created': '2017, 2, 14, 11, 39, 22, 99000)', u'post': u'ffffffffff', u'_id': ObjectId('58a2ec6a481f34192cb33d72'), u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 14, 11, 39, 22, 99000'}, 
		 {u'user_id': u'5891cced481f3416aa786783', u'date_modified': '2017, 2, 17, 11, 21, 45, 585000', u'likes': [ObjectId('5891cced481f3416aa786783')], u'date_created': '2017, 2, 17, 10, 21, 29, 319000', u'post': u'Pipi caca', u'_id': ObjectId('58a6cea9481f341c323fb3e8')}
	]


result = Core().InternalOperation("castDictObjectsId2DictHexIdRecursService", {"iter": po})
print result
print "------n-----------"
ids = "5898abfd481f3443d8917fce"
result = Core().InternalOperation("getCommunityPosts", {"community_id": ids})
print result

#http://192.168.1.176:8001/kayoo2/user/getUser?_id=5891cced481f3416aa786783
#http://192.168.1.176:8001/kayoo2/post/getCommunityPosts?id=5898abfd481f3443d8917fce
