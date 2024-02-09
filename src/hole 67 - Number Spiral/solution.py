m=[[0]*10for x in range(10)];y=i=-1;x=0
for a,b in[(0,1),(1,0),(0,-1),(-1,0)]*5:
	x+=a;y+=b
	while i<99:
		i+=1;m[x][y]=f"{i:>2}";x+=a;y+=b
		if x<0 or x>9or y<0 or y>9or m[x][y]:x-=a;y-=b;break
*map(print,[" ".join(r)for r in m]),
