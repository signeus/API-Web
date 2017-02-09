# Codigusiu derl kevin

def getAvatarByIdLegacy():
    _id = request.vars["_id"]
    core = Core()
    result = core.MediaOperation("getAvatarByIdLegacy", {"_id": _id})
    return response.stream(result)

def getAvatarById():
    _id = request.vars["_id"]
    Core().MediaOperation("getAvatarById", {
                                            "_id": _id,
                                            "response":response
                                            }
                         )
    return response.body.getvalue()