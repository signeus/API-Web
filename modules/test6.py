from core.core import Core

core = Core()
#getUserSuscribedCommunities
#print core.UserOperation("getByIdUser", {"_id":"5891cced481f3416aa786783"})
#print core.UserOperation("getUserSuscribedCommunities", {"_id":"5891cced481f3416aa786783"})
#print core.CommunityOperation("getUserSuscribedCommunities", {"_id":"5891cced481f3416aa786783"})
#58948f16481f342f73d3d0ab

#print core.UserOperation("suscribeUser2Community", {"id_user":"5891cd34481f3416aa786785","id_community":"58936e7c481f3408dea712ea"})
#print core.UserOperation("unsuscribeUser2Community", {"id_user":"5891cd34481f3416aa786785","id_community":"58945f60481f340f226a9ba1"})

#print core.UserOperation("unsuscribeUser2Community", {"id_user":"5891cced481f3416aa786783","id_community":"58948f16481f342f73d3d0ab"})
#print core.UserOperation("getByIdUser", {"_id":"5891cd34481f3416aa786785"})
#print core.UserOperation("deleteCommunityUnsuscribe", {"field":"communities_suscribed","_id":"58936e7c481f3408dea712ea"})


#589329df481f341a9db95828
#print core.UserOperation("suscribeUser2Community", {"id_user":"5891cd34481f3416aa786785","id_community":"5893723f481f340b515646a7"})
#print core.UserOperation("suscribeUser2Community", {"id_user":"5891ccb8481f3416aa786781","id_community":"5893723f481f340b515646a7"})
#print core.UserOperation("suscribeUser2Community", {"id_user":"5891cced481f3416aa786783","id_community":"5893723f481f340b515646a7"})
#result = core.PostOperation("getPostByCommunityId", {"community_id" : '5898b236481f3449bb923c94'})
result = core.PostOperation("getCommunityPosts", {"community_id" : '5898b236481f3449bb923c94'})
#result = core.UserOperation("getAllUsersFiltered", {'query':{}, 'filter':{'name':1, 'nick':1}})
print result
#print type(result)
#print result
