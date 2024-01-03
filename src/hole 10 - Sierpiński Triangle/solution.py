'''
explanation:
the function t return xth-order sierpinski triangle (x>=0) but upside down. the final print would flip the triangle right side up.
ranking as of 1/2/2024 200th in bytes. 202th in chars.
'''
def t(x):p=t(x-1)if x else 0;return[c+" "*(i+1)+c for i,c in enumerate(p)]+[" "*len(p)+c for c in p]if x else['▲']
print(*t(4)[::-1],sep="\n")
