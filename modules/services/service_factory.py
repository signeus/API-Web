# -*- coding: utf-8 -*-
from dbservices.user.create_user_service import CreateUserService
from dbservices.user.update_user_service import UpdateUserService
from dbservices.user.delete_user_service import DeleteUserService
from dbservices.user.get_all_user_service import GetAllUserService
from dbservices.user.get_by_id_user_service import GetByIdUserService
from dbservices.user.get_first_by_fields_user_service import GetFirstByFieldsUserService
from dbservices.user.unsubscribe_user_to_community_service import UnsubscribeUser2Community
from dbservices.user.subscribe_user_to_community_service import SubscribeUser2Community
from dbservices.user.get_user_subscribed_communities_service import GetUserSubscribedCommunitiesService
from dbservices.user.get_all_users_filtered_service import GetAllUsersFiltered
from dbservices.user.login_user_service import LoginUserService
from dbservices.user.sign_up_user_service import SignUpUserService
from dbservices.user.update_user_profile_service import UpdateUserProfileService
from dbservices.user.new_user_service import NewUserService
from dbservices.user.get_user_format_by_id_service import GetUserFormatByIdService
from dbservices.user.subscribe_user_service import SubscribeUserService
from dbservices.user.update_inside_fields_user_service import UpdateInsideFieldsUserService
from dbservices.user.extract_inside_fields_user_service import ExtractInsideFieldsUserService
from dbservices.user.find_user_service import FindUserService

from dbservices.community.create_community_service import CreateCommunityService
from dbservices.community.delete_community_service import DeleteCommunityService
from dbservices.community.delete_community_unsubscribe_service import DeleteCommunityUnsubscribeService
from dbservices.community.get_all_community_service import GetAllCommunityService
from dbservices.community.get_by_id_community_service import GetByIdCommunityService
from dbservices.community.get_first_by_fields_community_service import GetFirstByFieldsCommunityService
from dbservices.community.update_community_service import UpdateCommunityService
from dbservices.community.new_community_service import NewCommunityService
from dbservices.community.get_all_communities_service import GetAllCommunitiesService
from dbservices.community.get_communities_by_page_service import GetCommunitiesByPageService
from dbservices.community.get_communities_by_offset_service import GetCommunitiesByOffsetService
from dbservices.community.get_communities_service import GetCommunitiesService
from dbservices.community.count_community_members_service import CountCommunityMembersService
from dbservices.community.get_community_info_service import GetCommunityInfoService
from dbservices.community.get_community_users_service import GetCommunityUsersService
from dbservices.community.get_info_community_service import GetInfoCommunityService

from dbservices.post.create_post_service import CreatePostService
from dbservices.post.update_post_service import UpdatePostService
from dbservices.post.delete_post_service import DeletePostService
from dbservices.post.get_all_post_service import GetAllPostService
from dbservices.post.get_post_by_id_service import GetPostByIdService
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
from dbservices.post.check_post_urls_service import CheckPostUrlsService
from dbservices.post.check_content_type_url_service import CheckContentTypeUrlService
from dbservices.post.generate_embed_external_url_service import GenerateEmbedExternalUrlService
from dbservices.post.identify_external_url_service import IdentifyExternalUrlService
from dbservices.post.get_post_service import GetPostService
from dbservices.post.count_posts_service import CountPostsService
from dbservices.post.fav_post_service import FavPostService
from dbservices.post.user_fav_post_service import UserFavPostService
from dbservices.post.user_unfav_post_service import UserUnfavPostService
from dbservices.post.verify_read_post_service import VerifyReadPostService
from dbservices.post.new_survey_answer_service import NewSurveyAnswerService

from dbservices.validator.posts.post_attachment_service import PostAttachmentService

from dbservices.post.comment_2_post_service import Comment2PostService
from dbservices.post.get_comments_by_post_id_service import GetCommentsByPostId
from dbservices.post.get_comments_post_service import GetCommentsPost
from dbservices.post.count_comments_by_post_service import CountCommentsByPostService

from dbservices.post.new_repost_service import NewRepostService
from dbservices.post.get_repost_service import GetRepostService
from dbservices.post.count_repost_service import CountRepostService

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
from dbservices.media.exists_post_video_service import ExistsPostVideoService
from dbservices.media.exists_post_audio_service import ExistsPostAudioService
from dbservices.media.get_post_files_service import GetPostFilesService
from dbservices.media.save_post_video_service import SavePostVideoService
from dbservices.media.save_dir_video_service import SaveDirVideoService
from dbservices.media.save_video_service import SaveVideoService
from dbservices.media.get_post_video_by_id_service import GetPostVideoByIdService
from dbservices.media.get_dir_video_by_id_service import GetDirVideoByIdService
from dbservices.media.save_banner_service import SaveBannerService
from dbservices.media.save_default_banner_service import SaveDefaultBannerService
from dbservices.media.save_default__banner_image_service import SaveDefaultBannerImageService
from dbservices.media.get_post_audio_by_id_service import GetPostAudioByIdService
from dbservices.media.get_dir_audio_by_id_service import GetDirAudioByIdService
from dbservices.media.save_post_audio_service import SavePostAudioService
from dbservices.media.save_dir_audio_service import SaveDirAudioService
from dbservices.media.save_audio_service import SaveAudioService
from dbservices.media.get_random_post_comment_service import GetRandomPostCommentService

from dbservices.search.search_user_service import SearchUserService
from dbservices.search.search_post_service import SearchPostService
from dbservices.search.search_community_service import SearchCommunityService
from dbservices.search.search_all import SearchAllService
from dbservices.search.search_comment_service import SearchCommentService
from dbservices.search.find_service import FindService
from dbservices.search.find_user_service import FindUserService
from dbservices.search.find_community_service import FindCommunityService
from dbservices.search.find_post_service import FindPostService

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
from dbservices.caster.caster_cursor.cast_list_2_format_dict_service import CastList2FormatDictService
from dbservices.caster.caster_cursor.cast_dict_2_format_dict_service import CastDict2FormatDictService
from dbservices.caster.caster_diacritics.cast_diacritics_2_normalize import CastDiacritics2NormalizeService
from dbservices.caster.caster_diacritics.cast_normalize_2_diacritics import CastNormalize2DiacriticsService
from dbservices.caster.caster_format_text.cast_separate_text import CastSeparateTextService
from dbservices.caster.caster_format_text.cast_replace_text import CastReplaceTextService
from dbservices.caster.caster_format_text.cast_url_email_text import CastUrlEmailTextService

from dbservices.validator.validate_url_service import ValidateUrlService
from dbservices.validator.exists_url_service import ExistsUrlService

from dbservices.validator.find_everything_service import FindEverythingService

from dbservices.cleaner.clean_dictionary import CleanDictionaryService


class ServiceFactory (object):
    def __init__(self, core):
        self.core = core
        self.services = {
            ######Users#########
            "createUser"      			: CreateUserService,
            "updateUser"					: UpdateUserService,
            "deleteUser" 					: DeleteUserService,
            "getAllUser" 					: GetAllUserService,
            "getByIdUser"					: GetByIdUserService,
            "getFirstByFieldsUser" 			: GetFirstByFieldsUserService,
            "subscribeUser2Community"	: SubscribeUser2Community,
            "unsubscribeUser2Community"	: UnsubscribeUser2Community,
            "getUserSubscribedCommunities"	: GetUserSubscribedCommunitiesService,
            "getAllUsersFiltered"			: GetAllUsersFiltered,
            "loginUser"      				: LoginUserService,
            "signup"      					: SignUpUserService,
            "updateUserProfile"				: UpdateUserProfileService,
            "newUser"      					: NewUserService,
            "getUserFormatById"             : GetUserFormatByIdService,
            "subscribeUser"					: SubscribeUserService,
            "updateInsideFieldsUser"        : UpdateInsideFieldsUserService,
            "extractInsideFieldsUser"       : ExtractInsideFieldsUserService,
            "findUser"						: FindUserService,
            ######Communities#####
            "createCommunity" 			: CreateCommunityService,
            "updateCommunity"			: UpdateCommunityService,
            "deleteCommunity" 			: DeleteCommunityService,
            "deleteCommunityUnsubscribe" : DeleteCommunityUnsubscribeService,
            "getAllCommunity" 			: GetAllCommunityService,
            "getByIdCommunity"			: GetByIdCommunityService,
            "getFirstByFieldsCommunity" : GetFirstByFieldsCommunityService,
            "newCommunity" 				: NewCommunityService,
            "getAllCommunities"			: GetAllCommunitiesService,
            "getCommunitiesByPage"		: GetCommunitiesByPageService,
            "getCommunitiesByOffset"	: GetCommunitiesByOffsetService,
            "getCommunities"	        : GetCommunitiesService,
            "countCommunityMembers"		: CountCommunityMembersService,
            "getInfoCommunity"          : GetInfoCommunityService,
            "getCommunityInfo"			: GetCommunityInfoService,
            "getCommunityUsers"			: GetCommunityUsersService,
            ######Posts########
            "createPost" 			: CreatePostService,
            "updatePost"			: UpdatePostService,
            "deletePost" 			: DeletePostService,
            "getAllPost" 			: GetAllPostService,
            "getPostById"			: GetPostByIdService,
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
            "checkContentTypeUrl"           : CheckContentTypeUrlService,
            "generateEmbedExternalUrl"           : GenerateEmbedExternalUrlService,
            "identifyExternalUrl"           : IdentifyExternalUrlService,
            "postAttachment"                : PostAttachmentService,
            "countPosts"                    : CountPostsService,
            "favPost"                       : FavPostService,
            "userFavPost"                   : UserFavPostService,
            "userUnfavPost"                 : UserUnfavPostService,
            "verifyReadPost"                : VerifyReadPostService,
            "newSurveyAnswer"               : NewSurveyAnswerService,

            ##Repost##
            "newRepost"             : NewRepostService,
            "getPost"               : GetPostService,
            "getRepost"             : GetRepostService,
            "countRepost"           : CountRepostService,
            ##Comment##
            "comment2Post" 			: Comment2PostService,
            "getCommentsByPostId"	: GetCommentsByPostId,
            "getCommentsPost"		: GetCommentsPost,
            "countCommentsByPost"   : CountCommentsByPostService,
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
            "existsPostVideo"       : ExistsPostVideoService,
            "existsPostAudio"       : ExistsPostAudioService,
            "getPostFiles"		    : GetPostFilesService,
            "savePostVideo"			: SavePostVideoService,
            "saveDirVideo"			: SaveDirVideoService,
            "saveVideo"				: SaveVideoService,
            "getPostVideoById"      : GetPostVideoByIdService,
            "getDirVideoById"		: GetDirVideoByIdService,
            "saveBanner"			: SaveBannerService,
            "saveDefaultBanner"		: SaveDefaultBannerService,
            "saveDefaultBannerImage": SaveDefaultBannerImageService,
            "saveAudio"             : SaveAudioService,
            "saveDirAudio"          : SaveDirAudioService,
            "savePostAudio"         : SavePostAudioService,
            "getPostAudioById"      : GetPostAudioByIdService,
            "getDirAudioById"		: GetDirAudioByIdService,
            "checkPostUrls"			: CheckPostUrlsService,
            "getRandomPostComment"  : GetRandomPostCommentService,
            ######Search########
            "searchUserService" 		: SearchUserService,
            "searchPostService"         : SearchPostService,
            "searchCommunityService"    : SearchCommunityService,
            "searchAllService"          : SearchAllService,
            "searchCommentService"		: SearchCommentService,
            "find"                      : FindService,
            "findUser"                  : FindUserService,
            "findCommunity"             : FindCommunityService,
            "findPost"                  : FindPostService,

            #####Files#####
            "getFileTypeService"		: GetFileTypeService,
            #####Caster####
            "castDictObjectsId2DictHexId"			    : CastDictObjectsId2DictHexIdService,
            "castHex2ObjectId"						    : CastHex2ObjectIdService,
            "castListObjectsId2ListHexId"			    : CastListObjectsId2ListHexIdService,
            "castListDictObjectsId2ListDictHexId"	    : CastListDictObjectsId2ListDictHexIdService,
            "castObjectId2Hex"						    : CastObjectId2HexService,
            "castDictObjectsId2DictHexIdRecursService"  : CastDictObjectsId2DictHexIdRecursService,
            "castDiacritics2Normalize"                  : CastDiacritics2NormalizeService,
            "castNormalize2Diacritics"                  : CastNormalize2DiacriticsService,
            "castUrlEmailText"                          : CastUrlEmailTextService,
            "castSeparateText"                          : CastSeparateTextService,
            "castReplaceText"                           : CastReplaceTextService,

            ###Date###
            "castDictDate2DateTimestamp"			: CastDictDate2DateTimeStampService,
            "castListDate2DateTimestamp" 			: CastListDate2DateTimestampService,
            "castDate2DateTimestamp"				: CastDate2DateTimestampService,
            ###Cursor###
            "castList2FormatDict"				: CastList2FormatDictService,
            "castDict2FormatDict"				: CastDict2FormatDictService,
            ###Validator###
            "validateUrl"				: ValidateUrlService,
            "existsUrl"                 : ExistsUrlService,
            ###Cleaner###
            "cleanDictionary"           : CleanDictionaryService,
            ##Others##
            "findEverything"            : FindEverythingService,


        }

    def getTask(self, serviceName, parameters):
        return self.services[serviceName](self.core, parameters)
