# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def search():
   return response.json({"data":[{"search":"Tomate"},
     {"search": "Arroz"},
     {"search": "Berenjena"}], "result":0})