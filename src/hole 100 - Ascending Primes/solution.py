"""
explanation:
while loop generate candidate. sort. then check if candidate is a prime.
further explanation:
since candidate must be in ascending order there's only 2**9(512) options. biggest being 123456789 and each character can either be present or absent and thus why 2**9. 
the while loop create candidate by converting i(2~2**9) to binary and use 0 and 1 to represent the absent or present of the 9 numbers.
as of 01/02/2024 the code rank 35th in bytes and chars. 
"""
i,s,d=1,"123456789",[]
while i<512:d+=[int("".join(s[n]for n,i in enumerate(bin(i)[:1:-1])if i=="1"))];i+=1
for i in sorted(d)[1:]:
	if all(i%j for j in range(2,i)):print(i)
