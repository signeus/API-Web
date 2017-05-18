# -*- coding: utf-8 -*-

class ControllerParams (object):
    ######Admin#########
    def adminManageSubscriptions(self):
        return {"user_id"        :   "mandatory",
                "community_id"   :   "mandatory",
                "requested_user" :   "mandatory",
                "subscription"   :   "mandatory"
                }

    ######Community#########
    def newCommunity(self):
        return {"creator_id"               :  "mandatory",
                "community_type"           :  "mandatory",
                "leaders"                  :  "mandatory",
                "description"              :  "mandatory",
                "administrators"           :  "mandatory",
                "environment_type"         :  "mandatory",
                "name"                     :  "mandatory",
                "invitations"              :  "optional",
                "keywords"                 :  "optional",
                "inscription_validation"   :  "optional",
                "post_moderation"          :  "optional",
                "comment_disabled"         :  "optional",
                "masked_member_list"       :   "optional"
                }

    def getCommunities(self):
        return {"user_id" :   "mandatory",
                "start"   :   "optional",
                "offset"  :   "optional"
                }

    def getFirstByFieldsCommunity(self):
        return {"_id"  :   "mandatory"}

    def getByIdCommunity(self):
        return {"_id"   : "mandatory"}

    def deleteCommunity(self):
        return {"_id"   : "mandatory"}

    def updateCommunity(self):
        return {"_id"        : "mandatory",
                "new_values" : "mandatory"
                }

    def getAllCommunity(self):
        return {"user_id"    : "mandatory"}

    def getAllCommunities(self):
        return {"user_id"  : "mandatory",
                "start"    : "optional",
                "offset"   : "optional"
                }

    def getCommunityPosts(self):
        return {"id"       : "mandatory",
                "user_id"  : "mandatory"
                }

    def askForSubscribeCommunity(self):
        return {"community_id" : "mandatory",
                "user_id"      : "mandatory"
            }

    ######Post#########
    def getByIdPost(self):
        return {"id" : "mandatory"}

    def deletePost(self):
        return  {"id" : "mandatory"}

    def updatePost(self):
        return  {"id"         :   "mandatory",
                 "new_values" :   "mandatory"
                }

    def getPostsByCommunityId(self):
        return {"id"   :   "mandatory"}

    def getPostsByCommunityFormat(self):
        return {"id"    :  "mandatory"}
    def updatePostContent(self):
        return {"id"    :   "mandatory",
                "post"  :   "mandatory"
                }

    def like2Post(self):
        return {"user_id"   :   "mandatory",
                "id"        :   "mandatory"
                }
    def unlike2Post(self):
        return {"user_id"   :   "mandatory",
                "id"        :   "mandatory"
                }
    def likePost(self):
        return {"user_id"   :   "mandatory",
                "id"        :   "mandatory",
                "status"    :   "mandatory"
                }

    def comment2Post(self):
        return {"user_id"   :   "mandatory",
                "post_id"   :   "mandatory",
                "comment"   :   "mandatory",
                "files"     :   "optional"
                }

    def getCommentsByPost(self):
        return {"id"    :   "mandatory"}

    def getMainCommunityById(self):
        return {"id"    :    "mandatory"}

    def checkSurveyByPostId(self):
        return {"id"    :   "mandatory"}

    def getRepost(self):
        return {"id"    :   "mandatory"}

    def countRepost(self):
        return {"id"    :   "mandatory"}

    def countCommentsByPost(self):
        return {"id"    :    "mandatory"}

    def favPost(self):
        return {"user_id"   : "mandatory",
                "id"        : "mandatory",
                "status"    : "mandatory"
                }

    def newSurveyAnswer(self):
        return {"user_id"   : "mandatory",
                "post_id"   : "mandatory",
                "answer_id" : "mandatory"
                }

    def checkContentTypeUrl(self):
        return {"link"  : "mandatory"}

    def newRepost(self):
        return {"post_id"       :   "mandatory",
                "community_id"  :   "mandatory",
                "user_id"       :   "mandatory"
                }

    ######Search#########
    def searchUserService(self):
        return {"search"    :   "mandatory"}

    def searchPostService(self):
        return {"search"    :   "mandatory"}

    def searchCommunityService(self):
        return {"search"    :   "mandatory"}

    def searchCommentService(self):
        return {"search"    :   "mandatory"}

    def searchAllService(self):
        return {"search"    :   "mandatory"}

    def findUser(self):
        return {"search"    :   "mandatory"}

    def find(self):
        return {"search"    :   "mandatory"}

    ######User#########
    def loginUser(self):
        return {"mail"  :   "mandatory",
                "psswd" :   "mandatory"
                }

    def signup(self):
        return {"mail"  :   "mandatory",
                "psswd" :   "mandatory",
                "name"  :   "mandatory"
                }

    def updateUserProfile(self):
        return {"id"            :   "mandatory",
                "profileImage"  :   "optional"
                }

    def subscribeUser(self):
        return  {"user_id"      :   "mandatory",
                 "community_id" :   "mandatory",
                 "status"       :   "mandatory"
                 }

    def getFirstByFieldsUser(self):
        return {"_id"   :   "mandatory"}

    def getByIdUser(self):
        return {"_id"   :   "mandatory"}

    def deleteUser(self):
        return {"_id"   :   "mandatory"}

    def updateUser(self):
        return {"id"            :   "mandatory",
                "new_values"    :   "mandatory"
                }

    def subscribeUser2Community(self):
        return {"user_id"       :    "mandatory",
                "community_id"  :    "mandatory"
                }

    def getUser(self):
        return {"id"    :   "mandatory"}