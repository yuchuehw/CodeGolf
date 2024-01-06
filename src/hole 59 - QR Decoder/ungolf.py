import sys
qr=sys.argv[1].split("\n")
seq=[(20,8),(9,21)]*2+[(20,-1),(0,21)]+[(12,8),(9,13)]*2
b={"#":"0"," ":"1"}
d={"#":"1"," ":"0"}

step=-1
j=20
qrb=""
for s,e in seq:
	for i in range(s,e,step):
		if i==6:
			continue
		if(i+j)%2:
			qrb+=d[qr[i][j]]+b[qr[i][j-1]]
		else:
			qrb+=b[qr[i][j]]+d[qr[i][j-1]]
	step*=-1
	j-=3if j==8 else 2
c=""
for b in qrb[12:148]:
	c+=b
	if len(c)==8:print(chr(int(c,2)),end="");c=""
