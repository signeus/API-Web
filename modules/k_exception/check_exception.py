# -*- coding: utf-8 -*-

defined_errors = {
	"TOO_PARAMETERS" : "There are too many parameters for this operation",
	"EMPTY" : "There aren't parameters in this operation",
	"MANDATORY" : "The nexts parameters are mandatories",
}

class CheckException(Exception):
	def __init__(self, method, parameters, reason):
		self.method = method
		self.parameters = parameters
		self.reason = reason

	@property
	def message(self):
		msg = 'Exception: ' + defined_errors[self.reason]
		if len(self.parameters) > 0:
			values = ": "
			for k, v in self.parameters.iteritems():
				values += " " + k
			msg += values
		return msg
		
	def __str__(self):
		return self.message

