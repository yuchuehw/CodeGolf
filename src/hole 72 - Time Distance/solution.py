"""
as of 01/31/2024 ranked 95 in bytes and 30 in chrs
"""
import sys
l=1,60,60,24,7,30/7,12;u="second minute hour day week month".split()
for a in sys.argv[1:]:
	a=int(a);A=abs(a);t=""
	for i in range(6):
		A/=l[i]
		if A<l[i+1]:A=int(A);t+=f"{A} {u[i]}s"if A>1else f"a{''if i!=2else'n'} {u[i]}";break
	else:A=int(abs(a)/31536e3);t+=f"{A} years"if A>1else'a year'
	print("in "+t if a>0else t+" ago"if a else"now")
