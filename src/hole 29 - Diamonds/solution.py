def p(*i):print(*i,end="")
def q(n):
	p(" "*(9-n),i:=1)
	while i<n:p(i:=i+1)
	while i>1:p(i:=i-1)
	p("\n")
n=1
while n<10:
	i=0
	while i<n:q(i:=i+1)
	while i>1:q(i:=i-1)
	p("\n");n+=1
