import math

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
gcd = math.gcd(math.gcd(a, b), c)
if not (gcd == 1):
    a //= gcd
    b //= gcd
    c //= gcd
    print("gcd={} => a={} b={} c={}".format(gcd, a, b, c))
if b % c == 0:
    print(0)
for i in range(1, c + 1):
    if a * i % c == b % c:
        print(i, "+", str(c) + 'n')
