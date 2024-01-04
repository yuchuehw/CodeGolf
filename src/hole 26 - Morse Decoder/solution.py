"""
see the generation of string s in magic-s-generate.py
"""
import sys
s="..ETINAMSDRGUKWOHBLZFCP.VX.Q.YJ.56.7...8.......94.......3...2.10";d={s.index(i):i for i in s};r=str.replace
for w in sys.argv[1].split(" "*10):
	for c in w.split(" "*3):print(d[int("1"+r(r(r(c,"▄"*3,"1"),"▄","0")," ","")[::-1],2)],end="")
	print(" ",end="")
