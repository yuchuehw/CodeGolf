l=[0]
while len(l)<1001:print(i:=l[-1]);l+=[l[-2::-1].index(i)+1]if i in l[:-1]else[0]
