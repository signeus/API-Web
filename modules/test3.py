from services.dbservices.db_service import DBService
from casters.caster_object_id import CasterObjectId
#caster = CasterObjectId()
#print (caster.castHex2ObjectId('58821234481f341e70e68ce1'))

#print service.getFirstByFields({"_id" : caster.castHex2ObjectId('58821234481f341e70e68ce1'), 'id':'5'}, {}, "Communities")
result = DBService().getAllByFilter("Posts",{"community_id" : "5898ae82481f3445cb82c9ea"})
#result = DBService().getAllByFilter("Communities",{})

communities = [c for c in result]
CasterObjectId().castDictionaryObjectsId2DictionaryHexId(communities)
print communities 

"""
lista = [elem for elem in result]
result = []
for row in lista:
	rowResult = {}
	for key, value in row.iteritems():
		rowResult.update({str(key):value})
	result.append(rowResult)
print lista

for doc in result:
	print(doc)
"""
#whatIs = service.getById('58821234481f341e70e68ce1', "Communities")
#print whatIs

#nuevo = service.insertIn2Collection("Communities", {"test":"esto es una prueba", "name":"KTeam"})
#print nuevo
#print service.getAllOfCollection("Communities")

#service.insertIn2Collection("Communities", {"name":"Humanity", "other":"My property"})
#service.updateIn2Collection("Communities", "588b2e75481f340aa5c86207", {"other": "Modified my property"})
#service.getById('588b2e75481f340aa5c86207', "Communities")
#service.getAllOfCollection("Communities")
#service.getFirstByFields({'other':'Modified my property'}, {}, "Communities")
#service.deleteIn2Collection("Communities", "588b2e75481f340aa5c86207")
