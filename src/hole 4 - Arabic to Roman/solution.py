import sys
m,n,q=str.replace,divmod,'.c.cc.ccc.cb.b.bc.bcc.bccc.ca'.split('.');r="ⅩⅤⅠ","ⅭⅬⅩ","ⅯⅮⅭ"
def p(z):print(z,end="")
for(i)in sys.argv[1:]:
	k,l=n(int(i),1000);p(k*"Ⅿ");j=2
	while j>0:a,b,c=r[j];k,l=n(l,10**j);p(m(m(m(q[k],"a",a),"b",b),"c",c));j-=1
	a,b,c=r[0];print(m(m(m(q[l],"a",a),"b",b),"c",c))
