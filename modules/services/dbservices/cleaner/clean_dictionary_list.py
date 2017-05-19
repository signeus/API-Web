# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService


class CleanDictionaryListService(IService):
    def __init__(self, core, parameters):
        super(CleanDictionaryListService, self).__init__(core, parameters)
    def run(self):
        print "vamos a hacer clean diclist"
        list = [self.parameters.get("list", [])]
        keys =self.parameters.get("keys", [])
        field=self.parameters.get("field", "")
        print "esto es field"
        print field
        print "esto es keys"
        print keys
        for elem in list:
            print "----ENTRAMOS EN EL FOR----"

            for k,v in elem.iteritems():
                print "ANTES vamos a ver el valor..."
                print v
                print "esto es k"
                print k

                if k==field:
                    print "la clave es id"
                    if  type(v).__name__ =="ObjectId":
                        print "el valor es objid"
                        v = self.core.InternalOperation("castObjectId2Hex", {"id": v})
                       # elem[v]
                        # break
                        print "vamos a ver v"
                        print v
                        print "vamos a ver keys"
                        print keys
                        if v in keys:
                            print "esta ..."

                        else:
                            print "no estaaaaa"



            # print x
            # for key in keys:
            #     print key
            #     print "--->>>>>>>>>"
            #     if key in list["_id"]:
            #         print "entra en if"
            #         rb=[list[x]]
            #         print  "rb"
            #         print rb
        print "------------"
        print "LISTA FINAL"
        print list
        print "------------"
        return list
        #return {x: list[x] for x in list if x not in keys}

#
# for l in label:
#     if l['name'] == 'Test':
#         match = l
#         break
# else:
#      match = None
#
