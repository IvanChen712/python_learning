L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
L3 = [s.lower() if isinstance(s, str) else s for s in L1]

print(L1)
print(L2)
print(L3)
