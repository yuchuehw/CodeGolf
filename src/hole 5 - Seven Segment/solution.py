import sys;t=m=b=""
for n in sys.argv[1]:n=int(n);t+="   "if n in(1,4)else" _ ";m+=" "if n in(1,2,3,7)else"|";m+=" "if n in(0,1,7)else"_";m+=" "if n in(5,6)else"|";b+="|"if n in(0,2,6,8)else" ";b+=" "if n in(1,4,7)else"_";b+=" "if n==2else"|"
print("".join(t),"".join(m),"".join(b),sep="\n")
