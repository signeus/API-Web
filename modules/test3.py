from services.databases.db_service import DBService
#from casters.caster_object_id import CasterObjectId

service =  DBService()
#caster = CasterObjectId()
#print (caster.castHex2ObjectId('58821234481f341e70e68ce1'))

#print service.getFirstByFields({"_id" : caster.castHex2ObjectId('58821234481f341e70e68ce1'), 'id':'5'}, {}, "Communities")

#whatIs = service.getById(caster.castHex2ObjectId('58821234481f341e70e68ce1'), "Communities")
#print whatIs

nuevo = service.insertIn2Collection("Communities", {"test":"esto es una prueba", "name":"KTeam"})
print nuevo
#print service.getAllOfCollection("Communities")
