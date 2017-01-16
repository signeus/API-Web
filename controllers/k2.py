# -*- coding: utf-8 -*-

import json
from databases.test import Testencio
from pymongo import MongoClient

def getCommunity():
    valor = int("0")
    print request.vars["texto"]
    if "texto" in request.vars:
        print "Texto existe"
    for k,v in request.vars.iteritems():
        print k + " " + v
        valor = v
    return response.json({"Clave": valor,"Key":"Value"})

def testCan():
    test = Testencio()
    return test.testMethod()

def getDocument():
    file = open("/home/kevin/texto.txt","rt")
    return file.read()

def getJson():
    file = open("/home/kevin/jsonInput","rt")
    readed = file.read()
    parse2Json = json.loads(readed)
    return parse2Json

def getInfoDatabase():
    lista = []
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["lista"]
    #col.insert({"te":"pa"})
    #col.insert({"tu":"po"})
    for d in col.find({},{"_id":0}):
        lista.append(d)
    return response.json(lista)

def insertDatabase():
    connection = MongoClient("localhost", 27017)
    db = connection["warehouse"]
    col = db["Communities"]
    #print len(request.vars)
    print request.vars
    if len(request.vars) > 0:
        if "data" in request.vars:
            try:
                parse = json.loads(str(request.vars["data"]))
                print "Punto de ruptura manual"
                col.insert(parse)
            except Exception, e:
                print e
                print "Excepción controlada"
        '''for k,v in request.vars.iteritems():
            print k + " " + v
            try:
                parse = json.loads(v)
                col.insert({k:parse})
            except Exception , e:
                print "parse Error" TODO '''
    return "Todo ha sido guardado"

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
