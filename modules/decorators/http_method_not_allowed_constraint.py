from http.http_exception import HttpException

class HTTP_METHOD_NOT_ALLOWED_CONSTRAINT:
	def __init__(self, *args):
	    self.args = args

	def __call__(self, f):
		def wrapped_func():
			if self.args[0].env.request_method == 'OPTIONS':
				self.args[1].headers['Access-Control-Allow-Origin'] = '*'
				self.args[1].headers['Access-Control-Allow-Credentials'] = True
				self.args[1].headers['Access-Control-Allow-Headers']= "origin, content-type, accept"
				self.args[1].headers['Access-Control-Allow-Methods']= "GET, POST, OPTIONS, DELETE"
				return self.args[1].json({"Options":"ALLOWED"})
				#return None
			return f()
		return wrapped_func
