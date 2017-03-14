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
from dbservices.user.login_user_service import LoginUserService
from dbservices.user.sign_up_user_service import SignUpUserService
from dbservices.user.update_user_profile_service import UpdateUserProfileService
from dbservices.user.new_user_service import NewUserService

from dbservices.community.create_community_service import CreateCommunityService
from dbservices.community.delete_community_service import DeleteCommunityService
from dbservices.community.delete_community_unsuscribe_service import DeleteCommunityUnsuscribeService
from dbservices.community.get_all_community_service import GetAllCommunityService
from dbservices.community.get_by_id_community_service import GetByIdCommunityService
from dbservices.community.get_first_by_fields_community_service import GetFirstByFieldsCommunityService
from dbservices.community.update_community_service import UpdateCommunityService
from dbservices.community.new_community_service import NewCommunityService

from dbservices.post.create_post_service import CreatePostService
from dbservices.post.update_post_service import UpdatePostService
from dbservices.post.delete_post_service import DeletePostService
from dbservices.post.get_all_post_service import GetAllPostService
from dbservices.post.get_by_id_post_service import GetByIdPostService
from dbservices.post.get_first_by_fields_post_service import GetFirstByFieldsPostService
from dbservices.post.get_posts_by_community_id_service import GetPostsByCommunityIdService
from dbservices.post.get_posts_by_community_formated_service import GetPostsByCommunityFormatedService
from dbservices.post.get_community_posts_service import GetCommunityPostsService
from dbservices.post.user_like_post_service import UserLike2PostService
from dbservices.post.user_unlike_post_service import UserUnlike2PostService
from dbservices.post.like_post_service import Like2PostService
from dbservices.post.update_post_content_service import UpdatePostContentService
from dbservices.post.new_post_service import NewPostService
from dbservices.post.get_main_community_by_id_user_service import GetMainCommunityByIdService
from dbservices.post.check_survey_by_post_id_service import CheckSurveyByPostIdService
from dbservices.post.check_option_survey_service import CheckOptionSurveyService
from dbservices.post.uncheck_option_survey_service import UncheckOptionSurveyService
from dbservices.post.update_inside_fields_post_service import UpdateInsideFieldsPostService
from dbservices.post.extract_inside_fields_post_service import ExtractInsideFieldsPostService


from dbservices.post.comment_2_post_service import Comment2PostService
from dbservices.post.get_comments_by_post_id_service import GetCommentsByPostId
from dbservices.post.get_comments_post_service import GetCommentsPost


from dbservices.media.get_avatar_by_id_service import GetAvatarByIdService
from dbservices.media.get_banner_by_id_service import GetBannerByIdService
from dbservices.media.get_post_image_by_id_service import GetPostImageByIdService
from dbservices.media.get_dir_image_by_id_service import GetDirImageByIdService
from dbservices.media.get_avatar_by_id_legacy_service import GetAvatarByIdLegacyService
from dbservices.media.get_media_route_service import GetMediaRouteService
from dbservices.media.get_file_by_path_service import GetFileByPathService
from dbservices.media.get_files_routes_by_path_service import GetFilesRoutesByPathService
from dbservices.media.save_image_service import SaveImageService
from dbservices.media.save_avatar_service import SaveAvatarService
from dbservices.media.save_post_image_service import SavePostImageService
from dbservices.media.save_dir_image_service import SaveDirImageService
from dbservices.media.save_post_files_service import SavePostFilesService
from dbservices.media.save_file_service import SaveFileService
from dbservices.media.save_files_services import SaveFilesService
from dbservices.media.exists_file_service import ExistsFileService
from dbservices.media.exists_post_image_service import ExistsPostImageService
from dbservices.media.get_post_files_service import GetPostFilesService
from dbservices.media.save_post_video_service import SavePostVideoService
from dbservices.media.save_dir_video_service import SaveDirVideoService
from dbservices.media.save_video_service import SaveVideoService
from dbservices.media.get_post_video_by_id_service import GetPostVideoByIdService
from dbservices.media.get_dir_video_by_id_service import GetDirVideoByIdService

from services.filestype.get_file_type_service import GetFileTypeService

from dbservices.caster.caster_object_id.cast_dict_object_id_2_dict_hex_id_service import CastDictObjectsId2DictHexIdService
from dbservices.caster.caster_object_id.cast_dict_objects_id_2_dict_hex_id_recurs_service import CastDictObjectsId2DictHexIdRecursService
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
            "loginUser"      				: LoginUserService,
            "signup"      					: SignUpUserService,
			"updateUserProfile"				: UpdateUserProfileService,
            "newUser"      					: NewUserService,
            ######Communities#####
            "createCommunity" 			: CreateCommunityService,
            "updateCommunity"			: UpdateCommunityService,
            "deleteCommunity" 			: DeleteCommunityService,
            "deleteCommunityUnsuscribe" : DeleteCommunityUnsuscribeService,
            "getAllCommunity" 			: GetAllCommunityService,
            "getByIdCommunity"			: GetByIdCommunityService,
            "getFirstByFieldsCommunity" : GetFirstByFieldsCommunityService,
			"newCommunity" 				: NewCommunityService,
            ######Posts########
            "createPost" 			: CreatePostService,
			"updatePost"			: UpdatePostService,
			"deletePost" 			: DeletePostService,
			"getAllPost" 			: GetAllPostService,
			"getByIdPost"			: GetByIdPostService,
			"getFirstByFieldsPost" 	: GetFirstByFieldsPostService,
			"getPostsByCommunityId"		    : GetPostsByCommunityIdService,
			"getPostsByCommunityFormated"	: GetPostsByCommunityFormatedService,
			"getCommunityPosts"		: GetCommunityPostsService,
			"like2Post"				: UserLike2PostService,
            "unlike2Post"			: UserUnlike2PostService,
            "likePost"				: Like2PostService,
			"updatePostContent"		: UpdatePostContentService,
            "newPost" 				: NewPostService,
			"getMainCommunityById"	: GetMainCommunityByIdService,
			"checkSurveyByPostId"	: CheckSurveyByPostIdService,
			"checkOptionSurveyId"	: CheckOptionSurveyService,
			"uncheckOptionSurveyId"	: UncheckOptionSurveyService,
            "updateInsideFieldsPost"        : UpdateInsideFieldsPostService,
            "extractInsideFieldsPost"       : ExtractInsideFieldsPostService,

			#####Comment######
			"comment2Post" 			: Comment2PostService,
			"getCommentsByPostId"	: GetCommentsByPostId,
			"getCommentsPost"		: GetCommentsPost,
			######Media#######
			"getAvatarById"			: GetAvatarByIdService,
			"getBannerById"			: GetBannerByIdService,
			"getPostImageById"		: GetPostImageByIdService,
			"getDirImageById"		: GetDirImageByIdService,
			"getAvatarByIdLegacy"	: GetAvatarByIdLegacyService,
			"getMediaRoute"			: GetMediaRouteService,
			"saveImage"				: SaveImageService,
			"saveAvatar"			: SaveAvatarService,
			"savePostImage"			: SavePostImageService,
			"saveDirImage"			: SaveDirImageService,
			"getFileByPath"			: GetFileByPathService,
			"getFilesRoutesByPath"			: GetFilesRoutesByPathService,
			"savePostFiles"			: SavePostFilesService,
			"saveFile"				: SaveFileService,
			"saveFiles"				: SaveFilesService,
			"existsFile"			: ExistsFileService,
			"existsPostImage"		: ExistsPostImageService,
			"getPostFiles"		    : GetPostFilesService,
			"savePostVideo"			: SavePostVideoService,
			"saveDirVideo"			: SaveDirVideoService,
			"saveVideo"				: SaveVideoService,
            "getPostVideoById"      : GetPostVideoByIdService,
			"getDirVideoById"		: GetDirVideoByIdService,
			#####Files#####
			"getFileTypeService"		: GetFileTypeService,
			#####Caster####
			"castDictObjectsId2DictHexId"			    : CastDictObjectsId2DictHexIdService,
			"castHex2ObjectId"						    : CastHex2ObjectIdService,
			"castListObjectsId2ListHexId"			    : CastListObjectsId2ListHexIdService,
			"castListDictObjectsId2ListDictHexId"	    : CastListDictObjectsId2ListDictHexIdService,
			"castObjectId2Hex"						    : CastObjectId2HexService,
			"castDictObjectsId2DictHexIdRecursService"  : CastDictObjectsId2DictHexIdRecursService,
			    ###Date###
			"castDictDate2DateTimestamp"			: CastDictDate2DateTimeStampService,
			"castListDate2DateTimestamp" 			: CastListDate2DateTimestampService,
			"castDate2DateTimestamp"				: CastDate2DateTimestampService,
		}
		return services[serviceName](core, parameters)


	## def create_service(core, method, parameters):
	##	if(methodName == "newUser"):
	##		return UserService(core, parameters)
