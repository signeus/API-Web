# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import operator

class GetCommunityPostsService(IService):
    def __init__(self, core, parameters):
        super(GetCommunityPostsService, self).__init__(core, parameters)

    def run(self):
        _community_id = self.parameters.get("community_id", None)

        if not _community_id:
            raise Exception("Empty community ID is not allowed.")

        posts = self.core.InternalOperation("getPostsByCommunityFormated", {"community_id": _community_id})

        users = self.core.InternalOperation("getAllUsersFiltered", {'query': {}, 'filter': {'name': 1, 'nick': 1}})

        resultPosts = {}

        for key, value in posts.iteritems():
            ##URLS
            urlImage = posts[key].get("image","")
            if urlImage:
                posts[key]["image"] = {'url': posts[key]["image"], 'external':True}
            urlVideo = posts[key].get("video","")
            if urlVideo:
                posts[key]["video"] = {'url': posts[key]["video"], 'external':True}
            urlAudio = posts[key].get("audio","")
            if urlAudio:
                posts[key]["audio"] = {'url': posts[key]["audio"], 'external':True}

            #Likes
            likes = posts[key].pop("likes", [])
            for like in likes:
                posts[key]["likes"] = {}
                posts[key]["likes"][str(like)]  = {'name': users[str(like)].get("name", ""), 'nick': users[str(like)].get("nick", "")}


            ##Comments
            posts[key].update(users[str(value['user_id'])])
            comments = self.core.InternalOperation("getCommentsPost", {"post_id": key})
            posts[key]["comments"] = comments

            ##Image
            if self.core.InternalOperation("existsPostImage", {"id": key}): ##If exists...
                image = self.core.InternalOperation("getMediaRoute", {"service": "getPostImageById", "attribs": {"id": key}})
                posts[key]["image"] = {'url':image}
            ##Video
            if self.core.InternalOperation("existsPostVideo", {"id": key}):
                video = self.core.InternalOperation("getMediaRoute", {"service": "getPostVideoById", "attribs": {"id": key}})
                posts[key]["video"] = {'url':video}
            ##Audio
            if self.core.InternalOperation("existsPostAudio", {"id": key}):
                audio = self.core.InternalOperation("getMediaRoute", {"service": "getPostAudioById", "attribs": {"id": key}})
                posts[key]["audio"] = {'url':audio}
            ##Files
            files = self.core.InternalOperation("getPostFiles", {"id":key})
            if files:
               posts[key]["files"] = files

            ##Repost
            repost = posts[key].get("repost", None)
            if repost != None:
                repost = self.core.InternalOperation("getRepost", {"id": key})
                print repost
                resultPosts.update(repost)
                continue
                #deleteRepost = deleteRepost + [key]
                #self.updateKey(posts, repost.keys()[0], repost[repost.keys()[0]], key)

            resultPosts[key] = value
        # for key in deleteRepost:
        #     posts.pop(key,None)

        return resultPosts

    # def updateKey(self, dic, key, value, oldKey):
    #     operator.setitem(dic, key, value)