i,l=2,{}
while i<99:
	if all(i%j for j in l):l[i]=0;print(i)
	i+=1
