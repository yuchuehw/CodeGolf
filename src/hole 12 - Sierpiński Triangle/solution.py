'''
explanation:
the function t return xth-order sierpinski triangle (x>=0) but upside down. the final print would flip the triangle right side up.
ranking as of 1/30/2024 188th in bytes
'''
t=lambda x:[c+" "*(i+1)+c for i,c in enumerate(t(x-1))]+[" "*2**(x-1)+c for c in t(x-1)]if x else['▲'];*map(print,t(4)[::-1]),
# slightly more functional approach
# *map(print,(lambda a:lambda v:a(a,v))(lambda t,x:[c+" "*(i+1)+c for i,c in enumerate(t(t,x-1))]+[" "*2**(x-1)+c for c in t(t,x-1)]if x else['▲'])(4)[::-1]),
