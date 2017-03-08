# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetCommunityPostsService(IService):
    def __init__(self, core, parameters):
        super(GetCommunityPostsService, self).__init__(core, parameters)

    def run(self):
        posts = self.core.InternalOperation("getPostsByCommunityFormated", {"community_id": self.parameters['community_id']})
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

        return posts
