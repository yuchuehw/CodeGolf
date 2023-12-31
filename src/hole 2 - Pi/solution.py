"""
The following code uses a algorithm proposed in this SO post: https://stackoverflow.com/questions/9004789/1000-digits-of-pi-in-python
original by batbaatar
modified by yuchuehw
"""
_=[];q,r,t,k,m,x,j=1,0,1,1,3,3,0
while j<1e4:
	j+=1;z,q,r,t,k,m,x,y=(m,10*q,10*(r-m*t),t,k,(10*(3*q+r))//t-10*m,x,1)if(4*q+r-t<m*t)else(0,q*k,(2*q+r)*x,t*x,k+1,(q*(7*k+2)+r*x)//(t*x),x+2,0)
	if y:_.append(f"{z}")
print("3.","".join(_[1:1001]),sep="")
