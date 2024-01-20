l=[0,1];P=1
while len(l)<1e3:
	if l[P]==1:l+=[l[-1]]
	P+=1;l+=[1-l[-1]]
print(*[int(i)+1for i in l])
