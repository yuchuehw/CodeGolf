"""
ranked 68th in bytes and 25th in chrs as of 02/03/2024
"""
import sys;a=[];p=a.pop
for i in sys.argv[1:]:
	for c in i.split():a+=[int(eval(f"{p(-2)}{c}{p()}"))]if c in"+-*/"else[c]
	print(p())
