"""
see hole 26/magic-s-generate.py for design logic.
as of 01/04/2023 solution ranked 67th in bytes and 80th in chrs.
"""
import sys
s="..ETINAMSDRGUKWOHBLZFCP.VX.Q.YJ.56.7...8.......94.......3...2.10"
for w in sys.argv[1].split(" "):
	for c in w:print(bin(s.index(c))[3:][::-1].replace("0","▄ ").replace("1","▄"*3+" ")," ",end="")
	print(" "*7,end="")
