def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)

print(nwd(48, 18)) 