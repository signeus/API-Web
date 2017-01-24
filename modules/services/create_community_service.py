# -*- coding: utf-8 -*-
from interfaces.i_service import IService

class CreateCommunityService (IService):
	def __init__(self, core, parameters):
		super(CreateCommunityService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		connection = MongoClient("localhost", 27017)
		db = connection["warehouse"]
		col = db["Communities"]
		try:
			parse = json.loads(str(self.parameters["community"]))
			parse["date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			#col.insert(parse)
		except Exception, e:
			print e
			return "Ha habido un error al crear la comunidad"
		return "La comunidad ha sido creada"
