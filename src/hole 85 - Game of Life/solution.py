"""
rank 105th in bytes and chrs as of 01/05/2024
"""
import sys
m=[list(_)for _ in sys.argv[1].split("\n")];h=w=32;n=[[0]*h for _ in range(w)]
for i in range(h):
	for j in range(w):
		s,f=[-1,[2,3]]if m[i][j]=="#"else[0,[3]]
		for y,x in[(y,x)for y in range(i-1,i+2)for x in range(j-1,j+2)]:s+=1if(0<=x<h)and(0<=y<w)and m[y][x]=="#"else 0
		n[i][j]="#"if s in f else"."
print("\n".join(["".join(i) for i in n]))
