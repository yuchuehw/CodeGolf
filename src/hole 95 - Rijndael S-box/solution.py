t=[0]*256
x=1
for i in range(256):t[i]=x;x^=(x<<1)^((x>>7)*0x11B)
S=[0]*256
S[0]=99
for i in range(j:=255):x=t[j-i];x|=x<<8;x^=(x>>4)^(x>>5)^(x>>6)^(x>>7);S[t[i]]=(x^99)&j
for y in range(16):
    for x in range(16):print(f"{hex(S[16*y+x])[2:]:>02}",end=" ")
    print()
