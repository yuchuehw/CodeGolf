'''
ranked 116th as of 01/12/2024
'''
import sys
for a in sys.argv[1:]:
	A=a.upper();i=0;j=A[0]+A[A.rindex(' ')+1]if' 'in A else''
	for s in'las.z.G.ow.Ka.ui.ot.ur.pi.Mo.ev.sy.ee.xa.Vi'.split("."):j+='AK.AZ.GA.IA.KS.LA.MN.MO.MS.MT.NV.PA.TN.TX.VA'.split('.')[i]if s in a else'';i+=1
	for s in'deity':j+=A[0]+A[-1]if a.endswith(s)else''
	j=j+A[:2];print(j[:2])
