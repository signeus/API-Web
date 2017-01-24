# -*- coding: utf-8 -*-

from k_exception.check_exception import CheckException

class CHECK_PARAMETERS:
	def __init__(self, reqVars, params, method):
		self.reqVars = reqVars
		self.params = params
		self.method = method

	def __call__(self, function):
		def wrapped_func():
			### Empty parameters ###
			if len(self.reqVars) <= 0:
				try:
					raise CheckException(self.method, {}, "EMPTY")
				except Exception as ex:
					return ex
			### Mandatory Condition ###
			parameterMandatory = False
			for k, v in self.params.iteritems():
				if v == "mandatory":
					if not k in self.reqVars:
						parameterMandatory = True
			if parameterMandatory:
				try:
					raise CheckException(self.method, {k:v}, "MANDATORY")
				except Exception as ex:
					return ex
			### Too parameters ###
			cKsParams = set(self.params.keys())
			cKsReqVars = set(self.reqVars.keys())
			leftElems = cKsReqVars-cKsParams
			
			optionalParams = []
			for k, v in self.params.iteritems():
				if v == "optional":
					optionalParams.append(k)
			
			excessParams = {}
			for elem in leftElems:
				if not elem in optionalParams:
					excessParams.update({elem:"EXCESS"})
			if len(excessParams) > 0:
				try:
					raise CheckException(self.method, excessParams, "TOO_PARAMETERS")
				except Exception as ex:
					return ex
			
			return function()
		return wrapped_func
