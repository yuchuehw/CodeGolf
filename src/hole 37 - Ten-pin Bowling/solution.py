"""
assume all input is good. as of 01/11/2023 solution ranked 56 in bytes and 61 in chrs.
"""
import sys
for a in sys.argv[1:]:
	s=p=0;m=[1]*99;j=-1
	for c in a:
		j+=1
		if c==" ":continue
		m[1]+=1if c in"X/"and j<27else 0;m[2]+=1if c=="X"and j<27else 0;c=10 if c=="X"else 10-p if c=="/"else int(c)if 48<ord(c)<58else ord(c)-9311if ord(c)>1000else 0;s+=m.pop(0)*c;p=c
	print(s)
