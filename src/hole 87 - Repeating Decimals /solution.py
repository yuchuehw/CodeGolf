import sys;D=divmod
for a in sys.argv[1:]:
	i,j=[int(o)for o in a.split("/")];i,J=D(i,j);l=[0];L=[str(i)];i=J
	if i:l+=[0];L+=["."]
	while i:
		i*=10
		if i in l:L.insert(l.index(i),"(");L+=[")"];i=0
		elif i>=j:l+=[i];i,J=D(i,j);L+=[str(i)];i=J
		else:l+=[i];L+=['0']
	print("".join(L))
