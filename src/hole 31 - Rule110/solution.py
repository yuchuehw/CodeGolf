"""
took adventage of the fact 001 is same as 010. would not work otherwise.
"""
r=" ███ ██ "
print(s:=" "*99+"█")
for _ in range(99):print(s:="".join([r[int(s[j-1if j>0else 0:j+2].ljust(3).replace(" ","0").replace("█","1"),2)] for j in range(100)]))
