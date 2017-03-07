# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService
import base64
from PIL import Image
from io import BytesIO

class CreateCommunityService (IService):
    def __init__(self, core, parameters):
        super(CreateCommunityService, self).__init__(core, parameters)

    def run(self):
        try:
            return DBService(self.core).insertIn2Collection("Communities", self.parameters)
        except Exception, ex:
            print ex.message

