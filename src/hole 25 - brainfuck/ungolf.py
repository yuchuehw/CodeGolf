import sys
for ins in sys.argv[1:]:
	mem=[0];ip=mp=0
	while 1:
		i=ins[ip]
		if i==".":
			print(chr(mem[mp]),end="")
			ip+=1
		elif i=="+":
			mem[mp]+=1
			ip+=1
		elif i=="-":
			mem[mp]-=1
			ip+=1
		elif i==">":
			mp+=1
			mem+=[0]if len(mem)==mp else[]
			ip+=1
		elif i=="<":
			mp,mem=(mp-1,mem)if mp else(0,[0]+mem)
			ip+=1
		elif i in"[]":
			f=mem[mp]
			f,_,__,inc=[f==0,1,0,1]if i=="["else[f,0,1,-1]
			if f:
				while _!=__:
					ip+=inc
					if ins[ip]=="[":
						_+=1
					if ins[ip]=="]":
						__+=1
			ip+=1
		if ip==len(ins):
			break
