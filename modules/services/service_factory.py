# -*- coding: utf-8 -*-
#from dbservices.user.create_user_service import CreateUserService
from dbservices.community.create_community_service import CreateCommunityService
from dbservices.community.delete_community_service import DeleteCommunityService
from dbservices.community.get_all_community_service import GetAllCommunityService
from dbservices.community.get_by_id_community_service import GetByIdCommunityService
from dbservices.community.get_first_by_fields_community_service import GetFirstByFieldsCommunityService
from dbservices.community.update_community_service import UpdateCommunityService

class ServiceFactory (object):
	def __new__(cls, serviceName, core, parameters):
		services = {
			######Users#########
            "createUser"      			: CreateUserService,
            ######Communities#####
            "createCommunity" 			: CreateCommunityService,
            "updateCommunity"			: UpdateCommunityService,
            "deleteCommunity" 			: DeleteCommunityService,
            "getAllCommunity" 			: GetAllCommunityService,
            "getByIdCommunity"			: GetByIdCommunityService,
            "getFirstByFieldsCommunity" : GetFirstByFieldsCommunityService,
		}
		return services[serviceName](core, parameters)


	## def create_service(core, method, parameters):
	##	if(methodName == "newUser"):
	##		return UserService(core, parameters)
