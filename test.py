a = range(10)
b = filter(lambda x:x%2==0,a)
for x in b:
	print x,
c = reduce(lambda x,y:x+y, a)
print c
