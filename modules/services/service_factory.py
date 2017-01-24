# -*- coding: utf-8 -*-
from create_user_service import CreateUserService
from create_community_service import CreateCommunityService

class ServiceFactory (object):
	def __new__(cls, serviceName, core, parameters):
		services = {
			######Users#########
            "createUser" : CreateUserService,
            ######Communities#####
            "createCommunity" : CreateCommunityService,
		}
		return services[serviceName](core, parameters)


	## def create_service(core, method, parameters):
	##	if(methodName == "newUser"):
	##		return UserService(core, parameters)
