import sys
for a in sys.argv[1:]:
	s=0
	for i,c in enumerate(a.replace("-","")):s-=(10-i)*int(c)
	print(a+str(s%11).replace("10","X"))
