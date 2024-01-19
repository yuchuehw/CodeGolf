r=range(999);l=[];A=sorted
for x in r:
	for y in r:s,S=str(x),str(y);l+=[x*y]if len(s)==len(S)and A(s+S)==A(str(x*y))and x%10+y%10else[]
*map(print,A({*l})),
