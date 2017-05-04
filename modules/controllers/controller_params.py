# -*- coding: utf-8 -*-

class ControllerParams (object):
    ######Community#########
    def newCommunity(self):
        return {"creator_id":"mandatory", "community_type":"mandatory", "leaders[0]":"mandatory",
                    "description":"mandatory", "administrators[0]":"mandatory", "administrators[1]":"optional",
                    "administrators[2]":"optional", "administrators[3]":"optional", "administrators[4]":"optional",
                    "administrators[5]":"optional", "administrators[6]":"optional", "administrators[7]":"optional",
                    "administrators[8]":"optional", "administrators[9]":"optional",
                    "enviroment_type":"mandatory", "name":"mandatory", "invitations[0]":"optional", "invitations[1]":"optional",
                    "invitations[2]":"optional", "invitations[3]":"optional", "invitations[4]":"optional",
                    "keywords[0]":"optional", "keywords[1]":"optional", "keywords[2]":"optional"
                }

    def getCommunities(self): return {"user_id":"mandatory","start":"optional","offset":"optional"}
    def getFirstByFieldsCommunity(self):return {"_id":"optional"}
    def getByIdCommunity(self):return {"_id": "mandatory"}
    def deleteCommunity(self):return {"_id": "mandatory"}
    def updateCommunity(self): return {"_id": "mandatory", "new_values": "mandatory"}
    def getAllCommunity(self): return {"user_id": "mandatory"}
    def getAllCommunities(self): return {"user_id": "mandatory", "start": "optional", "offset": "optional"}

    ######Post#########
    def getByIdPost(self): return {"id": "mandatory"}
    def deletePost(self): return  {"id": "mandatory"}
    def updatePost(self): return {"id":"mandatory", "new_values":"mandatory"}
    def getPostsByCommunityId(self):return {"id":"mandatory"}
    def getPostsByCommunityFormat(self):return {"id":"mandatory"}
    def updatePostContent(self): return {"id": "mandatory", "post": "mandatory"}
    def like2Post(self): return {"user_id":"mandatory", "id":"mandatory"}
    def unlike2Post(self): return {"user_id":"mandatory", "id":"mandatory"}
    def likePost(self): return {"user_id": "mandatory", "id": "mandatory", "status": "mandatory"}
    def comment2Post(self): return {"user_id":"mandatory", "post_id":"mandatory", "comment":"mandatory","files":"optional"}
    def getCommentsByPost(self): return {"id":"mandatory"}
    def getMainCommunityById(self): return {"id": "mandatory"}
    def checkSurveyByPostId(self): return {"id":"mandatory"}
    def getRepost(self): return {"id": "mandatory"}
    def countRepost(self): return {"id":"mandatory"}
    def countCommentsByPost(self): return {"id": "mandatory"}
    def favPost(self): return {"user_id": "mandatory", "id": "mandatory", "status": "mandatory"}
    def newSurveyAnswer(self): return {"user_id": "mandatory", "post_id": "mandatory", "answer_id": "mandatory"}

    ######Search#########
    def searchUserService(self): return {"search":"mandatory"}
    def searchPostService(self): return {"search": "mandatory"}
    def searchCommunityService(self): return {"search": "mandatory"}
    def searchCommentService(self): return {"search": "mandatory"}
    def searchAllService(self): return {"search": "mandatory"}
    def findUser(self): return {"search": "mandatory"}
    def find(self): return {"search": "mandatory"}

    ######User#########
    def loginUser(self): return {"mail": "mandatory", "psswd": "mandatory"}
    def signup(self): return {"mail":"mandatory", "psswd":"mandatory", "name":"mandatory"}
    def updateUserProfile(self): return {"id":"mandatory", "profileImage":"optional"}
    def subscribeUser(self): return  {"user_id":"mandatory", "community_id":"mandatory", "status":"mandatory"}