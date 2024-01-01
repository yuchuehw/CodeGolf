import sys
a,b='.one.two.three.four.five.six.seven.eight.nine.ten.eleven.twelve.thirteen.fourteen.fifteen'.split('.'),'..twen.thir.for.fif'.split('.')
for n in sys.argv[1:]:s='';i,j=divmod(int(n),100);s+=''if i or j else"zero";s+="one thousand"if i==10 else f"{a[i]} hundred{' and 'if j else''}"if i else'';s+=a[j]if j<16 else f"{a[j-10]}teen"if j<20 else'';i,j=divmod(j,10);s+=f"{b[i] if i<6 else a[i]}ty{'-'if j else''}{a[j] if j else''}"if i>1 else'';print(s.replace('tt','t'))
