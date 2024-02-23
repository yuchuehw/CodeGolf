names = "MARY","PATRICIA","LINDA","BARBARA","ELIZABETH","JENNIFER,..."
print(sum((i+1)*sum(ord(c)-ord('A')+1for c in n)for i, n in enumerate(sorted(names))))
