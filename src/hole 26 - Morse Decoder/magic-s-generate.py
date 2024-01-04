"""
explanation:
the rationale is that we can treat morse code as binary number that is written from left to right. in the code i assume dot(▄) were 0 and dash(▄▄▄) were 1.
I then added a 1 at the end of all character since some have leading 0s. The string is thus the corresponding character at the corresponding index(in binary).
"""
d={
    "A": "▄ ▄▄▄",           "B": "▄▄▄ ▄ ▄ ▄",         "C": "▄▄▄ ▄ ▄▄▄ ▄",
    "D": "▄▄▄ ▄ ▄",         "E": "▄",                 "F": "▄ ▄ ▄▄▄ ▄",
    "G": "▄▄▄ ▄▄▄ ▄",       "H": "▄ ▄ ▄ ▄",           "I": "▄ ▄",
    "J": "▄ ▄▄▄ ▄▄▄ ▄▄▄",   "K": "▄▄▄ ▄ ▄▄▄",         "L": "▄ ▄▄▄ ▄ ▄",
    "M": "▄▄▄ ▄▄▄",         "N": "▄▄▄ ▄",             "O": "▄▄▄ ▄▄▄ ▄▄▄",
    "P": "▄ ▄▄▄ ▄▄▄ ▄",     "Q": "▄▄▄ ▄▄▄ ▄ ▄▄▄",     "R": "▄ ▄▄▄ ▄",
    "S": "▄ ▄ ▄",           "T": "▄▄▄",               "U": "▄ ▄ ▄▄▄",
    "V": "▄ ▄ ▄ ▄▄▄",       "W": "▄ ▄▄▄ ▄▄▄",         "X": "▄▄▄ ▄ ▄ ▄▄▄",
    "Y": "▄▄▄ ▄ ▄▄▄ ▄▄▄",   "Z": "▄▄▄ ▄▄▄ ▄ ▄",       "1": "▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "2": "▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄", "3": "▄ ▄ ▄ ▄▄▄ ▄▄▄",     "4": "▄ ▄ ▄ ▄ ▄▄▄",
    "5": "▄ ▄ ▄ ▄ ▄",       "6": "▄▄▄ ▄ ▄ ▄ ▄",       "7": "▄▄▄ ▄▄▄ ▄ ▄ ▄",
    "8": "▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄", "9": "▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄", "0": "▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
}
d2 = {}
for k,i in d.items():
    _ = int("1"+i.replace("▄▄▄","1").replace("▄","0").replace(" ","")[::-1],2)
    if _ in d2:
        print(_,k)
    else:
        d2[_] = k
s=""
for i in range(70):
    if i not in d2:
        s+="."
    else:
        s+=d2[i]
print(s)
