# -*- coding: utf-8 -*-

from services.interfaces.i_service import IService

class GetCommunityInfoService(IService):
    def __init__(self, core, parameters):
        super(GetCommunityInfoService, self).__init__(core, parameters)

    def run(self):
        id_comm=self.parameters["community_id"]
        communityInfo=self.core.InternalOperation("getByIdCommunity",{"_id": id_comm})
        usersInCommunity = self.core.InternalOperation("getCommunityUsers",
                                                  {"community_id":id_comm})
        listUsers=[]
        for i in usersInCommunity:
            x=self.core.InternalOperation("getByIdUser", {"_id": i["_id"]})
            dicUser = {}
            for k,v in x.iteritems():
                if k=="_id":
                    dicUser["_id"] = v
                if k=="name":
                    dicUser["name"]=v
                if k=="nick":
                    dicUser["nick"] = v
                if k=="avatar":
                    dicUser["avatar"] = v

            listUsers=listUsers+[dicUser]
            Users={}
            Users["Users"]=listUsers
            comm={}
            comm["Community"]=[communityInfo]
        allInfo = dict(Users, **comm)
        return allInfo
