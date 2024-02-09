f=lambda x:1if x<2else x*f(x-1)
for i in range(100):print(f(2*i)//f(i+1)//f(i))
