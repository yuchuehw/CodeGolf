"""
fewest bytes solution. ranked 111th as of 01/15/2023
"""
import sys
d={i:chr(j+128500)for i,j in zip("}(aDa:'-)a'DaX-)aO)a})a;-)aB-)aJa|a'(a\\a*aPa;-PaX-Pa@a:'-(aOa$aa(a)a#".split("a"),[-373,12,14,17,18,19,20,21,26,27,28,31,33,35,39,40,41,45,46,58,63,66,77,78,796])}
for a in sys.argv[1:]:print(d[a.replace(":-","")])
