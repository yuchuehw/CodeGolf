import sys
m=[[" "]*21 for _ in range(21)]
for k,i in{0:[0,1,2,3,4,5,6,14,15,16,17,18,19,20],1:[0,6,14,20],2:[0,2,3,4,6,8,14,16,17,18,20],3:[0,2,3,4,6,14,16,17,18,20],4:[0,2,3,4,6,14,16,17,18,20],5:[0,6,14,20],6:[0,1,2,3,4,5,6,8,10,12,14,15,16,17,18,19,20],7:[8],8:[0,1,2,4,5,6,7,8,13,14,18],10:[6],12:[6],13:[8],14:[0,1,2,3,4,5,6,8],15:[0,6,8],16:[0,2,3,4,6,8],17:[0,2,3,4,6],18:[0,2,3,4,6,8],19:[0,6,8],20:[0,1,2,3,4,5,6,8]}.items():
	for j in i:m[k][j]="#"
d,e=_=sys.argv[1].split(" ")
L=list("010000010001"+"".join([bin(ord(_))[2:].zfill(8)for _ in d])+"0000"+"".join([bin(int(i+j,16))[2:].zfill(8)for i,j in zip(e[::2],e[1::2])]));b={"0":"#","1":" "};d={"1":"#","0":" "};S=-1;j=20;q=c=""
for s,e in [(20,8),(9,21)]*2+[(20,-1),(0,21)]+[(12,8),(9,13)]*2:
	for i in range(s,e,S):
		if i==6:continue
		D,B=[d,b]if(i+j)%2else[b,d];m[i][j]=D[L.pop(0)];m[i][j-1]=B[L.pop(0)]
	S*=-1;j-=3if j==8else 2
print("\n".join(["".join(_) for _ in m]))
