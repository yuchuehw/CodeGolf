import sys
p=sys.stdout.write
p(" "*3+"2 3 4 5 6 7\n "+"-"*13)
for x in range(16):
	p(f"\n{hex(x)[2:].upper()}: ")
	for y in range(2,7if x>14else 8):
		p(chr(int(str(y)+hex(x)[2:],16))+" ")
p("DEL")
