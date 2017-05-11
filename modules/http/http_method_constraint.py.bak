from http_exception import HttpException

class HTTP_METHOD_CONSTRAINT:
	def __init__(self, *args):
		self.args = args
	
	def __call__(self, f):
		def wrapped_func():
			if str(self.args[1].env.request_method) != self.args[0]:
				raise HttpException(405)
			return f()
		return wrapped_func
