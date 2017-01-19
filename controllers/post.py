# -*- coding: utf-8 -*-

def insertPost():
    if len(request.vars) <= 0:
        return "No he recibido ningun post"
    if not "post" in request.vars:
        return "No he recibido ningun post"
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Posts"]
    try:
        parse = json.loads(str(request.vars["post"]))
        col.insert(parse)
    except Exception, e:
        print e
    return "Exito"

def getPosts():
    if not "id_community" in request.vars:
        return "No he recibido la id por parametro"
    listaPosts = []
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    for d in col.find({},{"_id":0}):
        lista.append(d)
    return response.json(lista)
    return "Exito"
