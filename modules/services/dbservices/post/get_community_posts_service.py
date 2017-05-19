# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from collections import OrderedDict


class GetCommunityPostsService(IService):
    def __init__(self, core, parameters):
        super(GetCommunityPostsService, self).__init__(core, parameters)

    def run(self):
        _community_id = self.parameters.get("community_id", None)
        _user_id = self.parameters.get("user_id", None)
        user = self.core.InternalOperation("getByIdUser", {"_id": _user_id})
        _community_ObjectId = self.core.InternalOperation("castHex2ObjectId", {"id": _community_id})
        user_communities_subscribed = user.get("communities_subscribed", [])

        if not _community_id:
            raise Exception("Empty community ID is not allowed.")
        if not _community_ObjectId in user_communities_subscribed:
            raise Exception("Community not visible for this  user ID.")
        if not _user_id:
            raise Exception("Empty user ID is not allowed.")


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
            # Favs
            favs = posts[key].pop("favs", [])
            for fav in favs:
                posts[key]["favs"] = {}
                posts[key]["favs"][str(fav)] = {'name': users[str(fav)].get("name", ""),
                                                      'nick': users[str(fav)].get("nick", "")}

            posts[key]["count_repost"] = self.core.InternalOperation("countRepost", {"post_id": key})
            ##Comments
            posts[key].update(self.core.InternalOperation("getUserFormatById", {"user_id": value['user_id']}))
                # Count of comments by post, that function depend on the Front now.
            #posts[key]["count_comments"] = self.core.InternalOperation("countCommentsByPost", {"post_id": key})
            comments = self.core.InternalOperation("getCommentsPost", {"post_id": key})
            posts[key]["comments"] = comments

            posts[key] = self.core.InternalOperation("postAttachment", {"post_id": key, "post": posts[key]})

            # ReadPost
            if self.core.InternalOperation("verifyReadPost", {"post_id": key, "user_id": _user_id}):
                posts[key]["read"] = True

            ##Repost
            repost = posts[key].get("repost", None)
            if repost != None:
                repost = self.core.InternalOperation("getRepost", {"id": key})
                urlIm = repost[repost.keys()[0]].get("image", "")
                if urlIm:
                    repost[repost.keys()[0]]["image"] = {'url': repost[repost.keys()[0]]["image"], 'external': True}
                urlVi = repost[repost.keys()[0]].get("video", "")
                if urlVi:
                    repost[repost.keys()[0]]["video"] = {'url': repost[repost.keys()[0]]["video"], 'external': True}
                urlAu = repost[repost.keys()[0]].get("audio", "")
                if urlAu:
                    repost[repost.keys()[0]]["audio"] = {'url': repost[repost.keys()[0]]["audio"], 'external': True}

                repost[repost.keys()[0]] = self.core.InternalOperation("postAttachment", {"post_id": repost.keys()[0],
                                                                                          "post": repost[
                                                                                              repost.keys()[0]]})
                # Likes
                lik = repost[repost.keys()[0]].pop("likes", [])
                for like in lik:
                    repost[repost.keys()[0]]["likes"] = {}
                    repost[repost.keys()[0]]["likes"][str(like)] = {'name': users[str(like)].get("name", ""),
                                                      'nick': users[str(like)].get("nick", "")}
                # Favs
                fv = repost[repost.keys()[0]].pop("favs", [])
                for fav in fv:
                    repost[repost.keys()[0]]["favs"] = {}
                    repost[repost.keys()[0]]["favs"][str(fav)] = {'name': users[str(fav)].get("name", ""),
                                                                        'nick': users[str(fav)].get("nick", "")}

                repost[repost.keys()[0]]["count_repost"] = self.core.InternalOperation("countRepost", {"post_id": repost.keys()[0]})
                resultPosts.update(repost)
                continue


            resultPosts[key] = value

        #print "------ANTES ORDEN ------------"
        #FALLA CUANDO ORDENA POST CON REPOST
        #resultPosts = OrderedDict(sorted(resultPosts.items(), key=lambda t: t[1]["date_modified"], reverse=True))

        #print "------FIN ------------"

        return resultPosts
