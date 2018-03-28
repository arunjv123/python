a = range(10)
b = filter(lambda x:x%2==0,a)
for x in b:
	print x,
c = reduce(lambda x,y:x+y, a)
print c
#this is a comment
name = raw_input("enter you name: ")
age = raw_input("enter you age: ")
if age > 18:
	print ("you are elligible to vote!", name)
else:
	print ("sorry. You can't vote now !", name)
