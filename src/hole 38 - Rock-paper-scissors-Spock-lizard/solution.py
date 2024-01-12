import sys
S="cuts📄covers💎crushes🦎poisons🖖smashes✂decapitates🦎eats📄disproves🖖vaporizes💎crushes✂";d={};p="✂";s=""
for c in S:
	if c.isalpha():s+=c
	else:d[p,c]=d[c,p]=p+" "+s+" "+c;p=c;s=""
for a in sys.argv[1:]:t=tuple(a);print(d[t]if t in d else"Tie")
