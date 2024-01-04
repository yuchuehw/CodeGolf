"""
see the generation of string s in magic-s-generate.py
as of 01/04/2023 solution ranked 61st in bytes and 74th in chrs.
"""
import sys
s="..ETINAMSDRGUKWOHBLZFCP.VX.Q.YJ.56.7...8.......94.......3...2.10";r=str.replace
for w in sys.argv[1].split(" "*10):
	for c in w.split(" "*3):print(s[int("1"+r(r(r(c,"▄"*3,"1"),"▄","0")," ","")[::-1],2)],end="")
	print(" ",end="")
