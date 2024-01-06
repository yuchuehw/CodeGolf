"""
as of 01/05/2023 rank 54th in chrs and bytes
"""
import sys
Q=sys.argv[1].split("\n");b={"#":"0"," ":"1"};d={"#":"1"," ":"0"};S=-1;j=20;q=c=""
for s,e in [(20,8),(9,21)]*2+[(20,-1),(0,21)]+[(12,8),(9,13)]*2:
	for i in range(s,e,S):
		if i==6:continue
		D,B=[d,b]if(i+j)%2else[b,d];q+=D[Q[i][j]]+B[Q[i][j-1]]
	S*=-1;j-=3if j==8else 2
for b in q[12:148]:
	c+=b
	if len(c)==8:print(chr(int(c,2)),end="");c=""
