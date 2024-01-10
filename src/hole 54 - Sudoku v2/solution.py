import sys
O=" 123456789";G=[[(i,j)for i in range(a,a+3)for j in range(b,b+3)]for a,b in[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]];n=[O.index(c) for c in sys.argv[1]if c in O];m=n[1::3];m=[m[i:i+9]for i in range(0,len(m),9)];M=[]
def v(m,p,v):return v in[m[i][j]for i,j in[g for g in G if p in g][0]] or v in m[p[0]] or v in[m[i][p[1]] for i in range(9)]
for x in range(99):
  for I in range(9):
  	C=[i for i in range(10)if i not in m[I]]
  	d={c:[]for c in C}
  	for i in range(9):
  		if m[I][i]!=0:continue
  		for c in C:
  			if v(m,(I,i),c)==0:d[c]+=[i]
  	for k,l in d.items():
  		if len(l)==1:m[I][l[0]]=k
for i in range(9):M.extend([str(j) for j in m[i]])
M=list(" "+"  ".join(M)+" ")
for c in sys.argv[1]:print(M.pop(0)if c in O else c,end="")
