"""
optimizaton of recursive Levenshtein distance algorithm from https://www.geeksforgeeks.org/introduction-to-levenshtein-distance/
as of 01/14/2024 ranked 110th in bytes.
"""
import sys
def l(s,S):i,j=s[:-1],S[:-1];return len(S)if s==""else len(s)if S==""else l(i,j)if s[-1]==S[-1]else 1+min(l(i,S),l(s,j),l(i,j))
for a in sys.argv[1:]:print(l(*a.split(" ")))
