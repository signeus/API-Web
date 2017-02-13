import urllib

class URLBuilder:
    def urlBuild(self, parametersApp):
        #protocol, ip, port, application, controller, {atribs}
        protocol = parametersApp.get('protocol', "http")
        ip = parametersApp.get('ip', "localhost")
        port = parametersApp.get('port', "80")
        application = parametersApp.get('application', "")
        controller = parametersApp.get('controller', "")
        attribs = parametersApp.get('attribs', {})
        urlCreated = '{protocol}://{ip}:{port}/{application}/{controller}'.format(
                                                                                    protocol=protocol,
                                                                                    ip=ip,
                                                                                    port=port,
                                                                                    application=application,
                                                                                    controller=controller
                                                                                 )

        if len(attribs) > 0:
            urlCreated = urlCreated + '?' + urllib.urlencode(attribs)

        return urlCreated

