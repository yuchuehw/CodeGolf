from itertools import*
from fractions import*
def r(l):
	L=[];n=len(l)-1
	for i,j in [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]]:
		if i>n or j>n:continue
		c=l[:];i=c.pop(i);j=c.pop(j);_=[i+j,i-j,j-i,i*j,i/j,j/i]
		if 24in _ and not c:return[]
		L+=[c+[i]for i in _ if i]
	return L
i=0
while i<1e4:
	i+=1;l=[Fraction((int(i)-10)%11)for i in f"{i:04}"]
	if sorted(l)==l:
		m=[l]
		for x in range(3):
			n=[]
			for o in m:
				p=r(o);n+=p
				if not p:print(*l);break
			m=n
