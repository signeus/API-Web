# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetCommunityPostsService(IService):
    def __init__(self, core, parameters):
        super(GetCommunityPostsService, self).__init__(core, parameters)

    def run(self):
        _community_id = self.parameters.get("community_id", None)

        if not _community_id:
            raise Exception("Empty community ID is not allowed.")

        posts = self.core.InternalOperation("getPostsByCommunityFormated", {"community_id": _community_id})

        users = self.core.InternalOperation("getAllUsersFiltered", {'query': {}, 'filter': {'name': 1, 'nick': 1}})
        for key, value in posts.iteritems():
            ##Comments
            posts[key].update(users[value['user_id']])
            comments = self.core.InternalOperation("getCommentsPost", {"post_id": key})
            posts[key]["comments"] = comments
            ##Image
            if self.core.InternalOperation("existsPostImage", {"id": key}): ##If exists...
                image = self.core.InternalOperation("getMediaRoute", {"service": "getPostImageById", "attribs": {"id": key}})
                posts[key]["image"] = image
            ##Video
            if self.core.InternalOperation("existsPostVideo", {"id": key}):
                video = self.core.InternalOperation("getMediaRoute", {"service": "getPostVideoById", "attribs": {"id": key}})
                posts[key]["video"] = video
            ##Audio
            if self.core.InternalOperation("existsPostAudio", {"id": key}):
                image = self.core.InternalOperation("getMediaRoute", {"service": "getPostAudioById", "attribs": {"id": key}})
                posts[key]["audio"] = image
            ##Files
            files = self.core.InternalOperation("getPostFiles", {"id":key})
            if files:
               posts[key]["files"] = files


        return posts
