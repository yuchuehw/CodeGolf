import sys
def l(s,S):i,j=s[:-1],S[:-1];return len(S)if s==""else len(s)if S==""else l(i,j)if s[-1]==S[-1]else 1+min(l(i,S),l(s,j),l(i,j))
for a in sys.argv[1:]:print(l(*a.split(" ")))
