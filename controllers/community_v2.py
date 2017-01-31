# -*- coding: utf-8 -*-
import json
from datetime import datetime

@HTTP_METHOD_CONSTRAINT("GET", request)
@CHECK_PARAMETERS(request.vars,{"id":"mandatory"},"getCommunity")
def getCommunity():
    if len(request.vars) <= 0:
        return "No he recibido ningún parametro"
    if not "id" in request.vars:
        return "No he recibido ningún Id"
    id = request.vars["id"]
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Communities"]
    value = col.find_one({"id": id},{"_id":0})
    return response.json(value)

@HTTP_METHOD_CONSTRAINT("GET", request)
def getCommunities():
    lista = []
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Communities"]
    lista = [elem for elem in col.find({},{"_id":0})]
    #for d in col.find({},{"_id":0}):
    #    lista.append(d)
    return response.json(lista)

#{id:ex, name:Java developer}
@HTTP_METHOD_CONSTRAINT("POST", request)
@CHECK_PARAMETERS(request.vars,{"community":"mandatory"},"newCommunity")
def newCommunity():
	myCore = Core()
	result = myCore.CommunityOperation("createCommunity", request.vars)
	return result

@HTTP_METHOD_CONSTRAINT("POST", request)
def updateCommunity():
    if len(request.vars) <= 1:
        return "No he recibido ningun parametro"
    if not "id" in request.vars:
        return "No he recibido ninguna Id"
    if not "name" in request.vars:
        return "No he recibido ningún parametro de modificación"
    id = request.vars["id"]
    name = request.vars["name"]
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Communities"]
    value = col.find_one_and_update({"id" : id},{'$set' : {'name': name}}, return_document=ReturnDocument.AFTER)
    return value

@HTTP_METHOD_CONSTRAINT("DELETE", request)
def deleteCommunity():
    if len(request.vars) <= 0:
        return "No he recibido ningun parametro"
    if not "id" in request.vars:
        return "No he recibido ningún id"
    id = request.vars["id"]
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Communities"]
    if col.count({"id": id}) <= 0:
        return "No existe ese registro"
    result = col.delete_one({"id": id})
    if result.deleted_count >= 1:
        return "Exito, comunidad eliminada"
    return "No ha sido eliminado ese elemento"
