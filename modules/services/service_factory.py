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
from dbservices.post.like_post_service import Like2PostService
from dbservices.post.unlike_post_service import Unlike2PostService

from dbservices.media.get_avatar_by_id_service import GetAvatarByIdService
from dbservices.media.get_avatar_by_id_legacy_service import GetAvatarByIdLegacyService
from dbservices.media.get_media_route import GetMediaRoute

from services.filestype.get_file_type_service import GetFileTypeService

from dbservices.caster.caster_object_id.cast_dict_object_id_2_dict_hex_id_service import CastDictObjectsId2DictHexIdService
from dbservices.caster.caster_object_id.cast_hex_2_object_id_service import CastHex2ObjectIdService
from dbservices.caster.caster_object_id.cast_list_objects_id_2_list_hex_id_service import CastListObjectsId2ListHexIdService
from dbservices.caster.caster_object_id.cast_list_dict_objects_id_2_list_dict_hex_id_service import CastListDictObjectsId2ListDictHexIdService
from dbservices.caster.caster_object_id.cast_object_id_2_hex_service import CastObjectId2HexService
from dbservices.caster.caster_datetime.cast_dict_date_2_date_timestamp_service import CastDictDate2DateTimeStampService
from dbservices.caster.caster_datetime.cast_list_date_2_date_timestamp_service import CastListDate2DateTimestampService
from dbservices.caster.caster_datetime.cast_date_2_date_timestamp_service import CastDate2DateTimestampService


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
			"getPostsByCommunityId"	: GetPostsByCommunityId,#TODO Service
			"getCommunityPosts"		: GetCommunityPosts,#TODO Service
			"like2Post"				: Like2PostService,
			"unlike2Post"			: Unlike2PostService,
			######Media#######
			"getAvatarById"			: GetAvatarByIdService,
			"getAvatarByIdLegacy"	: GetAvatarByIdLegacyService,
			"getMediaRoute"			: GetMediaRoute,#TODO Service
			#####Files#####
			"getFileTypeService"		: GetFileTypeService,
			#####Caster####
			"castDictObjectsId2DictHexId"			: CastDictObjectsId2DictHexIdService,
			"castHex2ObjectId"						: CastHex2ObjectIdService,
			"castListObjectsId2ListHexId"			: CastListObjectsId2ListHexIdService,
			"castListDictObjectsId2ListDictHexId"	: CastListDictObjectsId2ListDictHexIdService,
			"castObjectId2Hex"						: CastObjectId2HexService,
			    ###Date###
			"castDictDate2DateTimestamp"			: CastDictDate2DateTimeStampService,
			"castListDate2DateTimestamp" 			: CastListDate2DateTimestampService,
			"castDate2DateTimestamp"				: CastDate2DateTimestampService,
		}
		return services[serviceName](core, parameters)


	## def create_service(core, method, parameters):
	##	if(methodName == "newUser"):
	##		return UserService(core, parameters)
