import sys
L=[1,1];a,b=L
while a<2e19:a,b=b,a+b;L+=[b]
for a in sys.argv[1:]:
	b=a=int(a);l=L[::-1];f=0
	while l[0]>a:l.pop(0)
	for o in l:
		if f:f=0;continue
		if o<=a:print(f"{'+ 'if a!=b else''}{o} ",end="");f=1;a-=o
	print()
