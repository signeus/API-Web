

class Caller (object):
    def __init__(self, serviceName, parameters, serviceFactory):
        self.serviceName = serviceName
        self.parameters = parameters
        self.serviceFactory = serviceFactory

    def lastCall(self):
        try:
            serviceResult = self.serviceFactory.getTask(self.serviceName, self.parameters).run()
            return {'data': serviceResult, 'result':0}
        except Exception, ex:
            print '------'
            print ex
            print type(ex)
            print "Service: " + self.serviceName
            print '------'
            return {
                        "result": 1,
                        "data": {"message": ex.message, "error": 1, "type": 1},
                        "serviceName":self.serviceName,
                        "parameters" : self.parameters.keys()
                    }

    def call(self):
        try:
            return self.serviceFactory.getTask(self.serviceName, self.parameters).run()
        except Exception, ex:
            print '------'
            print ex
            print type(ex)
            print "Service: " + self.serviceName
            print '------'
            return {
                        "message": ex.message,
                        "serviceName": self.serviceName,
                        "parameters" : self.parameters.keys()
                    }