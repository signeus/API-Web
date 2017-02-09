# -*- coding: utf-8 -*-
from dbservices.user.create_user_service import CreateUserService
from dbservices.user.update_user_service import UpdateUserService
from dbservices.user.delete_user_service import DeleteUserService
from dbservices.user.get_all_user_service import GetAllUserService
from dbservices.user.get_by_id_user_service import GetByIdUserService
from dbservices.user.get_first_by_fields_user_service import GetFirstByFieldsUserService
from dbservices.user.unsuscribe_user_to_community_service import UnsuscribeUser2Community
from dbservices.user.suscribe_user_to_community_service import SuscribeUser2Community
from dbservices.user.get_user_suscribed_communities_service import GetUserSuscribedCommunities
from dbservices.user.get_all_users_filtered_service import GetAllUsersFiltered

from dbservices.community.create_community_service import CreateCommunityService
from dbservices.community.delete_community_service import DeleteCommunityService
from dbservices.community.delete_community_unsuscribe_service import DeleteCommunityUnsuscribeService
from dbservices.community.get_all_community_service import GetAllCommunityService
from dbservices.community.get_by_id_community_service import GetByIdCommunityService
from dbservices.community.get_first_by_fields_community_service import GetFirstByFieldsCommunityService
from dbservices.community.update_community_service import UpdateCommunityService

from dbservices.post.create_post_service import CreatePostService
from dbservices.post.update_post_service import UpdatePostService
from dbservices.post.delete_post_service import DeletePostService
from dbservices.post.get_all_post_service import GetAllPostService
from dbservices.post.get_by_id_post_service import GetByIdPostService
from dbservices.post.get_first_by_fields_post_service import GetFirstByFieldsPostService
from dbservices.post.get_posts_by_community_id_service import GetPostsByCommunityId
from dbservices.post.get_community_posts_service import GetCommunityPosts

class ServiceFactory (object):
	def __new__(cls, serviceName, core, parameters):
		services = {
			######Users#########
            "createUser"      				: CreateUserService,
			"updateUser"					: UpdateUserService,
			"deleteUser" 					: DeleteUserService,
			"getAllUser" 					: GetAllUserService,
			"getByIdUser"					: GetByIdUserService,
			"getFirstByFieldsUser" 			: GetFirstByFieldsUserService,
			"suscribeUser2Community"		: SuscribeUser2Community,
			"unsuscribeUser2Community"		: UnsuscribeUser2Community,
			"getUserSuscribedCommunities"	: GetUserSuscribedCommunities,
			"getAllUsersFiltered"			: GetAllUsersFiltered,
            ######Communities#####
            "createCommunity" 			: CreateCommunityService,
            "updateCommunity"			: UpdateCommunityService,
            "deleteCommunity" 			: DeleteCommunityService,
            "deleteCommunityUnsuscribe" : DeleteCommunityUnsuscribeService,
            "getAllCommunity" 			: GetAllCommunityService,
            "getByIdCommunity"			: GetByIdCommunityService,
            "getFirstByFieldsCommunity" : GetFirstByFieldsCommunityService,
            ######Posts########
            "createPost" 			: CreatePostService,
			"updatePost"			: UpdatePostService,
			"deletePost" 			: DeletePostService,
			"getAllPost" 			: GetAllPostService,
			"getByIdPost"			: GetByIdPostService,
			"getFirstByFieldsPost" 	: GetFirstByFieldsPostService,
			"getPostsByCommunityId"	: GetPostsByCommunityId,
			"getCommunityPosts"		: GetCommunityPosts,
		}
		return services[serviceName](core, parameters)


	## def create_service(core, method, parameters):
	##	if(methodName == "newUser"):
	##		return UserService(core, parameters)
