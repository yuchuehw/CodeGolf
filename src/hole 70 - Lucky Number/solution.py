print(len([*range(1,8810,i:=2)]))
l=[0]+[*range(1,8810,i:=2)];print(1)
while i<1001:
	print(j:=l[i])
	for o in l[::j][1:]:l.remove(o)
	i+=1
