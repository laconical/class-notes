def sqr(x):
	return x*x
def differential(f):
	return lambda x: (f(x+0.001)-f(x))/0.001

a=differential(sqr)
print a(3)

