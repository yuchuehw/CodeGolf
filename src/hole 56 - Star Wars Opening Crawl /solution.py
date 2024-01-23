"""
as of 01/22/2023 55th for bytes and 27th in chr(compressed)
"""
import sys
R=str.replace
Z=print
B=" "
for a in sys.argv[1:]:
	P=lambda:a.pop(0);a=R(a,"\n"," | ").split(B);s=int(P());c=int(P());P()
	for i in range((s+1)*2):
		S=""
		while a and a[0]!="|"and len(S+a[0])<=c:S+=P()+B
		if S:
			S=S[:-1]
			if B in S and a and a[0]!="|":D,M=divmod(c-len(S),S.count(B));p=B*(D+1);S=R(R(S,B,p),p,p+B,M)
			Z(B*s+S)
		elif a:Z();P()
		if i%2:s-=1;c+=2
	Z()

#compressed code:
#exec(bytes('浩潰瑲猠獹刊猽牴爮灥慬散娻瀽楲瑮䈻∽∠昊牯愠椠⁮祳⹳牡癧ㅛ崺਺倉氽浡摢㩡⹡潰⡰⤰愻刽愨∬湜Ⱒ•⁼⤢献汰瑩䈨㬩㵳湩⡴⡐⤩挻椽瑮倨⤨㬩⡐਩昉牯椠椠⁮慲杮⡥猨ㄫ⨩⤲਺उ㵓∢ऊ眉楨敬愠愠摮愠せ⅝∽≼湡⁤敬⡮⭓孡崰㰩挽区㴫⡐⬩ੂउ晩匠਺उ匉匽㩛ㄭ੝उ椉⁦⁂湩匠愠摮愠愠摮愠せ⅝∽≼䐺䴬搽癩潭⡤ⵣ敬⡮⥓匬挮畯瑮䈨⤩瀻䈽⠪⭄⤱医刽刨匨䈬瀬ⰩⱰ⭰ⱂ⥍ऊउ⡚⩂⭳⥓ऊ攉楬⁦㩡⡚㬩⡐਩उ晩椠㈥猺㴭㬱⭣㈽ऊ⡚ ','u16')[2:])
