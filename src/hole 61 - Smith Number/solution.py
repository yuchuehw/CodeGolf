"""
as of 01/21 ranked 56th in bytes and 20th in chr (bytes version)
"""
i=3
while i<1e4:
	i+=1;j=i;s=""
	for k in range(2,i):
		while j/k==j//k:j/=k;s+=str(k)
	if sum(map(int,str(i)))==sum(map(int,s)):print(i)

## byte version ##
# exec(bytes('㵩ਲ਼桷汩⁥㱩攱㨴ऊ⭩ㄽ樻椽猻∽ਢ昉牯欠椠⁮慲杮⡥ⰲ⥩਺उ桷汩⁥⽪㵫樽⼯㩫⽪欽猻㴫瑳⡲⥫ऊ晩猠浵洨灡椨瑮猬牴椨⤩㴩猽浵洨灡椨瑮猬⤩瀺楲瑮椨 ','u16')[2:])
