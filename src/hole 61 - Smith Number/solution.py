"""
as of 01/21 ranked 56th in bytes and 20th in chr (bytes version)
"""
i=3
while i<1e4:
	i+=1;j=i;s=""
	for k in range(2,i):
		while j/k==j//k:j/=k;s+=str(k)
	if sum(map(int,str(i)))==sum(map(int,s)):print(i)
