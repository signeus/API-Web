# -*- coding: utf-8 -*-
import json

def prueba():
    return request.env.request_method

@HTTP_METHOD_CONSTRAINT("GET", request)
def getCommunity():
    valor = int("0")
    print request.vars["texto"]
    if "texto" in request.vars:
        print "Texto existe"
    for k,v in request.vars.iteritems():
        print k + " " + v
        valor = v
    return response.json({"Clave": valor,"Key":"Value"})

def insertCommunity():
    if len(request.vars) <= 0:
        return "No he recibido ningun parametro"
    if not "community" in request.vars:
        return "No he recibido ninguna comunidad"
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Communities"]
    try:
        parse = json.loads(str(request.vars["community"]))
        col.insert(parse)
    except Exception, e:
        print e
    return "Exito"

def getCommunities():
    lista = []
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Communities"]
    for d in col.find({},{"_id":0}):
        lista.append(d)
    return response.json(lista)
