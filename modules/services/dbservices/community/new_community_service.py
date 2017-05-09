# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
from k_exception.invalid_fields_exception import InvalidFieldsException
class NewCommunityService (IService):
    def __init__(self, core, parameters):
        super(NewCommunityService, self).__init__(core, parameters)

    def run(self):
        image = self.parameters.get("banner", None)
        self.parameters.pop("banner", None)
        listMandatory=["name", "description", "leaders", "administrators", "creator_id", "environment_type", "community_type"]
        fieldsKO=[]
        for k,v  in self.parameters.iteritems():
            for i in listMandatory:

                if k==i:
                    value=str(v).strip()
                    if len(value)==0:
                        print k + " esta vacio"
                        fieldsKO.append(i)


        if len(fieldsKO)>0:
            raise InvalidFieldsException(fieldsKO)

        for k, v in self.parameters.iteritems():
            if k=="name":
                nameFound=DBService(self.core).getAllByFilter("Communities",
                                                        {k: v})
                if len(nameFound)>0:
                    raise Exception("EL NOMBRE DE LA COMUNIDAD YA EXISTE")
            elif k=="community_type":
                if int(v)>2:
                    raise Exception("Exception: Invalid community_type")
            elif k == "environment_type":
                if int(v)>1:
                    raise Exception("Exception: Invalid environment_type")


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
