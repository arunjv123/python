a = range(10)
b = filter(lambda x:x%2==0,a)
for x in b:
	print x,
c = reduce(lambda x,y:x+y, a)
print c
i =0
while i < len(a):
	b = a[i]**2
	i = i+1

print b
