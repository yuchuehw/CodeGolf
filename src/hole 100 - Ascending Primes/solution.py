i,s,d=1,"123456789",{}
while i<2**9:d[int("".join([s[n]for n,i in enumerate(bin(i)[2:][::-1])if i=="1"]))]= 0;i+=1
for i in sorted(d)[1:]:
	if all(i%j for j in range(2,i)):print(i)
