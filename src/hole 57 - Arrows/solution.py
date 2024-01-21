import sys
l=[-1,0,0,1,1,0,0,-1,-1]+[1]*4+[-1]*3
m='\\8N]9O^:P_;Qb\x18>c\x19?\x00\x1b@\x01\x1aA'
c=0,0
for a in sys.argv[1:]:
	a=chr(ord(a)%100)
	if a in m:i,j=c;_=m.index(a)//3*2;I,J=l[_:_+2];c=i+I,j+J
	print(*c)
