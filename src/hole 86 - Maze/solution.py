# ranked 86th in bytes and 65th in chrs as of 02/13/2024
import sys
m=[];r=[]
for i,l in enumerate(sys.argv[1].split("\n")):r+=[[(i,l.index("S"))]]if"S"in l else[];m+=[list(l)]
h,w=len(m),len(m[0])
while 1:
	R=[]
	for _ in r:
		i,j=_[-1]
		for x,y in(1,0),(-1,0),(0,1),(0,-1):
			X,Y=i+x,j+y;P=(X,Y)
			if 0<=X<h and 0<=Y<w and m[X][Y]!="#" and P not in _:
				R.append(_+[P])
				if m[X][Y]=="E":
					for x,y in _[1:]:m[x][y]="."
					print("\n".join(["".join(i)for i in m]));exit()
	r=R
