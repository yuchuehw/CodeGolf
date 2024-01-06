f=[0]*997
for i in range(1,1001):
    for j in range(2,997):
        while i//j==i/j:i=i//j;f[j]+=1
for i,j in enumerate(f):
    if j:print(f"{f'{i}^{j}'if j>1 else f'{i}'}*",end="")
print(997)
