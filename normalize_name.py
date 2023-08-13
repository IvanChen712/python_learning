def normalize(name):
    # return name[0].upper() + name[1:].lower()
    return name.title()


# example usage
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
