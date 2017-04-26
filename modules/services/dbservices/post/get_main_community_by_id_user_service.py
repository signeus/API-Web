# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class GetMainCommunityByIdService(IService):
    def __init__(self, core, parameters):
        super(GetMainCommunityByIdService, self).__init__(core, parameters)

    def run(self):
        userId = self.parameters.get("user_id","")
        user = self.core.InternalOperation("getUserSuscribedCommunities", {"_id": userId})
        allUsers = self.core.InternalOperation("getAllUsersFiltered", {'query': {}, 'filter': {'name': 1, 'nick': 1}})
        communities = user.get("communities_subscribed",[])
        if len(communities) == 0:
            return ""

        postsDict = {}
        for elem in communities:
            posts = self.core.InternalOperation("getPostsByCommunityId", {"community_id": elem['id']})
            for post in posts:
                _id = str(post.pop('_id', '')) #Extract the ID
                #Inserting comments
                comments = self.core.InternalOperation("getCommentsPost", {"post_id": _id}) #Retrieve the comments of this post
                post["comments"] = comments

                user_id = str(post.pop('user_id', '')) #Extract the User
                allUsers[user_id]["user_id"] = user_id
                post = dict(post,**allUsers[user_id]) #Merged user with the post
                post["community_name"] = elem["name"] #Inserted the community name
                post["community_id"] = elem["id"] #Inserted the community ID
                postsDict[_id] = post
        return postsDict
