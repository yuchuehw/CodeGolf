for i in range(7):
	print(" "*(2+i)+"█"+"─"*(4*(i+1))+"█")
	for j in range(i+1):print(" "*(i+1-j)+"╱"+" "*(4*(i+1))+"╱"+" "*j+"│")
	print('█'+'─'*(4*(i+1))+'█'+' '*(i+1)+'│')
	for j in range(2*i+2):print('│'+" "*(4*(i+1))+"│"+" "*(2*i-j+1 if j>i else i+1)+("█"if j==i else"╱"if j>i else"│"))
	print("█"+"─"*(4*(i+1))+"█\n")
