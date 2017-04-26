from timeit import timeit

lis = [1,2,3,4,5]
o = []
m = []
#o = {"t":"e", "s":"e"}
#m = {"o":"z", "e":"h"}

def metodo1():
	for elem in lis:
		elem *= 2
		o.append(elem)
	return o

def metodo2():	
	mi = [2*elem for elem in lis]
	return mi

def metodo3(m,o):
	mo = m + o
	return mo

def metodo4():	
	for k,v in o.iteritems():
		print k + " " + v
	
def metodo5():
	m = {k:v for k, v in o.iteritems()}
	print m	
	
	
#print timeit(metodo1,number = 1) 
#print timeit(metodo2,number = 1)
#print metodo3(metodo1(), metodo2())
#print metodo4()
#print metodo5()

#print timeit(metodo4,number = 1) 
#print timeit(metodo5,number = 1)




u={}
u= u.get("u","o")
print u
