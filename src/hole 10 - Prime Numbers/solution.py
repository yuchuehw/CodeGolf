i=2
while i<99:
	if all(i%j for j in range(2,i-1)):print(i)
	i+=1
