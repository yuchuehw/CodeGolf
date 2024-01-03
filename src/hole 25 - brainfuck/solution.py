import sys
for s in sys.argv[1:]:
	m=[0];p=q=0
	while 1:
		i=s[p]
		if i==".":print(chr(m[q]),end="")
		elif i in"+-":exec(f"m[q]{i}=1")
		elif i==">":q+=1;m+=[0]if len(m)==q else[]
		elif i=="<":q,m=(q-1,m)if q else(0,[0]+m)
		elif i in"[]":
			f=m[q];f,_,__,c=[f==0,1,0,1]if i=="["else[f,0,1,-1]
			if f:
				while _!=__:p+=c;_+=1if s[p]=="["else 0;__+=1if s[p]=="]"else 0
		p+=1
		if p==len(s):break
