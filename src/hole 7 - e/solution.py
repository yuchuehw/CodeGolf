import fractions
F=fractions.Fraction;H=F(1,2)
def r(n):r=n.numerator//n.denominator;e=n-F(r);r+=1 if e>H or(e==H and r&1==1)else 0;return r
a,s,f,i=1000,F(0),1,0;t=10 ** a;_=F(t)
while 1:
    m=F(1,f)
    s+=m
    if i>=1 and f>t:
        l=r(s*_)
        u=r((s+m)*_)
        if l==u:s=str(l);print(s[:len(s)-a]+"."+s[len(s)-a:]);break
    i+=1;f*=i
