"""
as of 01/27/2024 ranked 70th in bytes and 47th in chr
"""
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

# compressed
# exec(bytes('浩潰瑲猠獹䰊∽⁁䄠⁳時䈠䌠⁦⁃獂䌠⁳晄䐠†獄䔠⁦⁅晆䘠䔠⁳獆䜠⁦⁇䜠⁳晁∠爮灥慬散∨≳挬牨㤨㌸⤹⸩敲汰捡⡥昢Ⱒ档⡲㠹㜳⤩氊䰽献汰瑩∨∠਩㵬稪灩氨㩛㈺ⱝ孬㨱㈺⥝ਬ潦⁲⁡湩猠獹愮杲孶㨱㩝ऊ㵁⹡灳楬⡴㬩㵳⩻䱛㩛⹌湩敤⡸⭟•⤢⹝潣湵⡴•⤢⼯昲牯张椠⁮嵁㭽㵏∢ऊ潦⁲⁯湩猠਺उ潦⁲Ⱪⱪ⁫湩㌨㘬挬牨ㄨ㘷⤩⠬ⰳⰷ洢⤢⠬ⰴⰷ∢㨩ऊउ晩⩻潛⠬⭯⥩ㄥⰲ漨樫┩㈱絝㴽㩳Ᵽ㵃孬嵯伻⠽⁣晩挠椠⁮⁡汥敳䌠⬩੫昉牯椠椠⁮㩁ऊ弉漽摲椨せ⥝㘭ਵउ晩⩻潛⠬⭯⤴ㄥⰲ漨㠫┩㈱絝㴽⁳湡⁤档⡲弨㈫┩⬷㔶椩⁮⁡湡⁤档⡲弨㐫┩⬷㔶椩⁮㩡⭏椽∫∫ऊ牰湩⡴⥏','u16')[2:])
