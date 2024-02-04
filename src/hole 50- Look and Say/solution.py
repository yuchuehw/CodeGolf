S="1"
for x in range(20):
	print(s:=S);p=s[0];C=0;S=""
	for c in s:
		if c==p:C+=1
		else:S+=f"{C}{p}";p=c;C=1
	S+=f"{C}{p}"
