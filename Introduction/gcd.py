def gcd(a, b):
    if(a < b):
        a, b = b, a
    while(b!=0):
        t = a
        a = b
        b = t % b
    return a

print(gcd(60, 96))
print(gcd(20, 8))

# note that if a < b, the first loop will effectively swap the two
# therefore no need to add a comparison at the beginning
def gcd_simplified(a, b):
    while(b!=0):
        t = a
        a = b
        b = t % b
    return a
