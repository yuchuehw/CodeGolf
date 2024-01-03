"""
create a lookup table d that map all valid character to ascii representation.
as of 01/03/2023 code rank 71st in bytes and 83rd in chr.
note:code assume notations are all valid.
"""
import sys
d={"/":"\n"}
for i in range(12):d.update({"KQRBNPkqrbnp"[i]:chr(9812+i),str(i):" "*i})
for a in sys.argv[1:]:
	for c in a.split(" ")[0]:print(d[c],end="")
	print("\n")
