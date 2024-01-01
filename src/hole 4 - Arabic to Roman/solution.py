import sys
m,n,o,q=str.replace,divmod,list,{9:"ca",8:"bccc",7:"bcc",6:"bc",5:"b",4:"cb",3:"ccc",2:"cc",1:"c",0:""};r=o("ⅩⅤⅠ"),o("ⅭⅬⅩ"),o("ⅯⅮⅭ")
def p(z):print(z,end="")
for(i)in sys.argv[1:]:
	k,l=n(int(i),1000);p(k*"Ⅿ");j=2
	while j>0:a,b,c=r[j];k,l=n(l,10**j);p(m(m(m(q[k],"a",a),"b",b),"c",c));j-=1
	a,b,c=r[0];print(m(m(m(q[l],"a",a),"b",b),"c",c))
