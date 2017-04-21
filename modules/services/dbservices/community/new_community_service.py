# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewCommunityService (IService):
    def __init__(self, core, parameters):
        super(NewCommunityService, self).__init__(core, parameters)

    def run(self):
        # print "RUN"
        # image = self.parameters.get("banner", None)
        # self.parameters.pop("banner", None)
        # listMandatory=[]
        # for k,v  in self.parameters.iteritems():
        #     print "esto es k"
        #     print k
        #     field={}
        #     if k=="description" or k=="name":
        #         field[k]="mandatory"
        #
        #     print field
        #

        ## x=trim(self.parmeters.get("description", None))
        ## if x
        # 
        record = self.core.InternalOperation("createCommunity",self.parameters)
        userInfo = self.core.InternalOperation("subscribeUser2Community",
                                             {"user_id": record["creator_id"], "community_id": record["_id"], "creator_id":record["creator_id"]})

        id = record.get("_id", None)

        if not id:
            raise Exception("New community, Not exists the ID to generate the image.")

        if image:
            urlImage = self.core.InternalOperation("saveBanner", {'id':id, 'data':image})
            record['image'] = urlImage
        else:
            description = record.get("description", "")
            keywords = record.get("keywords", [])
            urlImage = self.core.InternalOperation("saveDefaultBanner", {'id':str(id), 'description': description, 'keywords':keywords})
            record['image'] = urlImage

        record["communities_subscribed"] = userInfo.get("communities_subscribed",[])

        return record
