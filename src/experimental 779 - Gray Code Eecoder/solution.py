"""
implementing the reflect-and-prefix method.(https://en.wikipedia.org/wiki/Gray_code#/media/File:Binary-reflected_Gray_code_construction.svg)
"""
import sys
for n in sys.argv[1:]:
	l=["0","1"];n=int(n)
	while len(l)<=n:l=["0"+o for o in l]+["1"+o for o in l][::-1]
	print(l[n])
