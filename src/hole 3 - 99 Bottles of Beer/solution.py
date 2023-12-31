i=99
while i>-1:print(f"{i if i else 'No more'} bottle{'s' if i!=1 else ''} of beer on the wall, {i if i else 'no more'} bottle{'s' if i!=1 else ''} of beer.");print(f"Take one down and pass it around, {i-1 if i-1 else 'no more'} bottle{'s' if i-1!=1 else ''} of beer on the wall.\n" if i>0 else "Go to the store and buy some more, 99 bottles of beer on the wall.");i-=1
