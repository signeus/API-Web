# -*- coding: utf-8 -*-

def getAvatarByIdLegacy():
    _id = request.vars["id"]
    core = Core()
    result = core.MediaOperation("getAvatarByIdLegacy", {"_id": _id})
    return response.stream(result)

def getAvatarById():
    _id = request.vars["id"]
    Core().MediaOperation("getAvatarById", {
                                            "_id": _id,
                                            "response":response
                                            }
                         )
    return response.body.getvalue()

##Used by Front##
def getPostImageById():
    request.vars["response"] = response
    Core().MediaOperation("getPostImageById", request.vars)
    return response.body.getvalue()

def getBannerById():
    _id = request.vars["id"]
    Core().MediaOperation("getBannerById", {
                                            "_id": _id,
                                            "response":response
                                            }
                         )
    return response.body.getvalue()

def savePostFiles():
    mediaRoutes = Core().MediaOperation("savePostFiles", dict(request.vars))
    return mediaRoutes


def getMediaRoute():
    _service = request.vars.get("service", "nonService")
    _attribs = request.vars.get("attribs", {})
    mediaRoute = Core().MediaOperation("getMediaRoute", {
                                                        "serviceName"   :  _service,
                                                        "attribs"       :  _attribs
                                                        }
                                      )
    return mediaRoute

def getFileByPath():
    request.vars["response"] = response
    Core().MediaOperation("getFileByPath", dict(request.vars))
    return response.body.getvalue()