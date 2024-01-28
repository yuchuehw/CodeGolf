import sys
L="A  A♯ B♭ B C♭ C B♯ C♯ D♭ D  D♯ E♭ E F♭ F E♯ F♯ G♭ G  G♯ A♭ "
l=L.split(" ")
l=*zip(l[::2],l[1::2]),
for a in sys.argv[1:]:
	A=a.split();s={*[L[:L.index(_+" ")].count(" ")//2for _ in A]};O=""
	for o in s:
		for i,j,k in(3,6,"°"),(3,7,"m"),(4,7,""):
			if{*[o,(o+i)%12,(o+j)%12]}==s:c,C=l[o];O=c+k if c in a else C+k
	for i in A:
		_=ord(i[0])-65
		if{*[o,(o+4)%12,(o+8)%12]}==s and chr((_+2)%7+65)in a and chr((_+4)%7+65)in a:O+=i+"+"
	print(O)
