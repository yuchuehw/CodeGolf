s="1"
while(l:=len(s))<1000:s+=str(max(sum(s[-i:]*j==s[-i*j:]for j in range(5))for i in range(l)))
*map(print,s),
