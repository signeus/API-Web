from route_builder.url_builder import URLBuilder

class MediaEnrouting:
    def __init__(self, resourceManagerParameters):
        self.rmp = resourceManagerParameters
        self.protocol = resourceManagerParameters["protocol_app"]
        self.ip = resourceManagerParameters["ip_app"]
        self.port = int(resourceManagerParameters["port_app"])
        self.name = resourceManagerParameters["name_app"]

    def getMedia2External(self, serviceName, attribs):
        url = URLBuilder().urlBuild({
                                        'protocol':self.protocol,
                                        'ip':self.ip,
                                        'port':self.port,
                                        'application':self.name,
                                        'controller':serviceName,
                                        'attribs': attribs
                                     }
                                     )
        return url