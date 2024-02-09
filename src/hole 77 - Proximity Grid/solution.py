import sys
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ";S="0123456789"+s+s.lower()+"-"
for A in sys.argv[1:]:
	def I(x,y,v):
		if-1<x<9and-1<y<9and(t:=A[x][y])in S and v<=S.index(t):A[x][y]=S[v];I(x-1,y,v+1);I(x,y-1,v+1);I(x+1,y,v+1);I(x,y+1,v+1)
	A=[[*_]for _ in A.split()];[I(i,j,0)for i in range(9)for j in range(9)if A[i][j]=="0"];*map(print,[''.join(i)for i in A]+['']),
