from decimal import*
getcontext().prec=1100
l=[0,1];P=1;S=0;A=Decimal(1)
while len(l)<1e7:
	if l[P]==1:l+=[l[-1]]
	P+=1;l+=[1-l[-1]]
for i in l[1:]:
	A/=2
	if i:S+=A
print(str(S)[:1002])
