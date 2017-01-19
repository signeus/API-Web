# -*- coding: utf-8 -*-

import json
from databases.test import Testencio
import base64


def testCan():
    test = Testencio()
    return test.testMethod()

def getDocument():
    file = open("/home/kevin/texto.txt","rt")
    return file.read()

def getFileInBytes():
    file = open("/home/kevin/Notebook.3DS","rb")
    return file.read()

def getFileEncoding():
    name = "Notebook.3DS"
    file = open("/home/kevin/" + name, "rb" ).read()
    encodeFile = base64.b64encode(file)
    #response.headers["Content-Type"] = "application/octet-stream"
    response.headers["Content-Type"] = "application/octet-stream"
    return response.json({name:encodeFile})

def getFileDecoding():
    if len(request.vars) <= 0:
        return "No he recibido ningun parametro"
    if not "file" in request.vars:
        return "No he recibido ningún archivo"
    encodeStr = str(request.vars["file"])
    encodeFile = base64.b64decode(file)
    response.headers["Content-Type"] = "application/octet-stream"
    return encodeFile

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
