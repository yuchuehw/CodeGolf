"""
implemetation of the reflect-and-prefix method but backward.(https://en.wikipedia.org/wiki/Gray_code#/media/File:Binary-reflected_Gray_code_construction.svg)
101 = 100 - 001
111 = 111 - 011
...etc
"""
import sys
def d(g):return 0if g=="0"else 1if g=="1"else 2**len(g)-1-d(g[1:])if g[0]=="1" else d(g[1:])
for arg in sys.argv[1:]:print(d(arg))
