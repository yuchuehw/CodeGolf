            import sys
            for ins in sys.argv[1:]:
                ins=[_ for _ in ins if _ in"[<=.,->]"]
                mem=[0];ip=mp=0
                while 1:
                    i=ins[ip]
                    if i==",":
                        mem[mp]=ord(input()[0])
                    if i==".":
                        print(chr(mem[mp]),end="")
                    elif i in"+-":
                        exec(f"mem[mp]{i}=1")
                    elif i==">":
                        mp+=1
                        mem+=[0]if len(mem)==mp else[]
                    elif i=="<":
                        mp,mem=(mp-1,mem)if mp else(0,[0]+mem)
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
