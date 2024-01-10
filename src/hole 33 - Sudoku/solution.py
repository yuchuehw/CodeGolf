"""
the code could only solve simple sudoku puzzle
"""
import sys
G=[[(i,j)for i in range(a,a+3)for j in range(b,b+3)]for a,b in[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]];m=[[int(c)if c.isdigit()else 0 for c in l]for l in sys.argv[1:]]
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
def p(*x):print(*x,end="")
def z(s):
	i=1;a,b,c,d,e=s
	while i<10:p(a*3+(b if i%3else c if i%9else d+e));i+=1	
p("┏");z("━┯┳┓\n");i=1;j=1
for r in m:
	p("┃");j=1
	for n in r:p("",n,"│"if j%3 else"┃");j+=1
	if i==9:break
	p("\n┠"if i%3 else "\n┣");s="─┼╂┨\n"if i%3else"━┿╋┫\n";z(s);i+=1
p("\n┗");z("━┷┻┛\n")
