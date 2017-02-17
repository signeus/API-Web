# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from casters.caster_object_id import CasterObjectId
from casters.caster_datetime import CasterDatetime
from casters.caster_cursor import CasterCursor


class GetCommunityPosts(IService):
    def __init__(self, core, parameters):
        super(GetCommunityPosts, self).__init__(core, parameters)

    def run(self):
        posts = self.core.InternalOperation("getPostsByCommunityId", {"community_id": self.parameters['community_id']})
        users = self.core.InternalOperation("getAllUsersFiltered", {'query': {}, 'filter': {'name': 1, 'nick': 1}})
        for key, value in posts.iteritems():
            posts[key].update(users[value['user_id']])
            #TODO Include webservice of image
        return posts
