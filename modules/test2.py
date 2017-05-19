"""from core.core import Core

c= Core()
p = c.UserOperation("createUser", {})
print p
"""

from decorators.check_parameters import CHECK_PARAMETERS


@CHECK_PARAMETERS({"pepe":"tomate", "tsa":"tomate"},{"pepe":"mandatory","test":"optional"},"getCommunity")
def prueba():
	print "caca"

try:
	prueba()
except Exception as ex:
	print ex
