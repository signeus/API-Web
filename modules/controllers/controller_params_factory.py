# -*- coding: utf-8 -*-
from controller_params import ControllerParams

class ControllerParamsFactory (object):
    def __init__(self):
        self.controllerParams=ControllerParams()

        self.controllers = {
            ######Admin#########
            "adminManageSubscriptions"      : self.controllerParams.adminManageSubscriptions(),
            ######Community#########
            "newCommunity"      			: self.controllerParams.newCommunity(),
            "getCommunities"                : self.controllerParams.getCommunities(),
            "getFirstByFieldsCommunity"     : self.controllerParams.getFirstByFieldsCommunity(),
            "getByIdCommunity"              : self.controllerParams.getByIdCommunity(),
            "deleteCommunity"               : self.controllerParams.deleteCommunity(),
            "updateCommunity"               : self.controllerParams.updateCommunity(),
            "getAllCommunity"               : self.controllerParams.getAllCommunity(),
            "getAllCommunities"             : self.controllerParams.getAllCommunities(),
            "askForSubscribeCommunity"      : self.controllerParams.askForSubscribeCommunity(),
            ######Post#########
            "getByIdPost"                   : self.controllerParams.getByIdPost(),
            "deletePost"                    : self.controllerParams.deletePost(),
            "updatePost"                    : self.controllerParams.updatePost(),
            "getPostsByCommunityId"         : self.controllerParams.getPostsByCommunityId(),
            "getPostsByCommunityFormat"     : self.controllerParams.getPostsByCommunityFormat(),
            "updatePostContent"             : self.controllerParams.updatePostContent(),
            "like2Post"                     : self.controllerParams.like2Post(),
            "unlike2Post"                   : self.controllerParams.unlike2Post(),
            "likePost"                      : self.controllerParams.likePost(),
            "comment2Post"                  : self.controllerParams.comment2Post(),
            "getCommentsByPost"             : self.controllerParams.getCommentsByPost(),
            "getMainCommunityById"          : self.controllerParams.getMainCommunityById(),
            "checkContentTypeUrl"           : self.controllerParams.checkContentTypeUrl(),
            "checkSurveyByPostId"           : self.controllerParams.checkSurveyByPostId(),
            "getRepost"                     : self.controllerParams.getRepost(),
            "countRepost"                   : self.controllerParams.countRepost(),
            "countCommentsByPost"           : self.controllerParams.countCommentsByPost(),
            "favPost"                       : self.controllerParams.favPost(),
            "newSurveyAnswer"               : self.controllerParams.newSurveyAnswer(),
            "getCommunityPosts"             : self.controllerParams.getCommunityPosts(),
            "newRepost"                     : self.controllerParams.newRepost(),
            ######Search#########
            "searchUserService"             : self.controllerParams.searchUserService(),
            "searchPostService"             : self.controllerParams.searchPostService(),
            "searchCommunityService"        : self.controllerParams.searchCommunityService(),
            "searchCommentService"          : self.controllerParams.searchCommentService(),
            "searchAllService"              : self.controllerParams.searchAllService(),
            "findUser"                      : self.controllerParams.findUser(),
            "find"                          : self.controllerParams.find(),
            ######User#########
            "loginUser"                     : self.controllerParams.loginUser(),
            "signup"                        : self.controllerParams.signup(),
            "updateUserProfile"             : self.controllerParams.updateUserProfile(),
            "subscribeUser"                 : self.controllerParams.subscribeUser(),
            "getFirstByFieldsUser"          : self.controllerParams.getFirstByFieldsUser(),
            "getByIdUser"                   : self.controllerParams.getByIdUser(),
            "deleteUser"                    : self.controllerParams.deleteUser(),
            "updateUser"                    : self.controllerParams.updateUser(),
            "subscribeUser2Community"       : self.controllerParams.subscribeUser2Community(),
            "getUser"                       : self.controllerParams.getUser(),
            "changeUserLanguage"            : self.controllerParams.changeUserLanguage()

        }

    def getParams(self, controllerName):
        return self.controllers[controllerName]