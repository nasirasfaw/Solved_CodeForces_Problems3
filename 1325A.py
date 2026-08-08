from math import gcd
from math import lcm
t = int(input())
for _ in range(t):
    x = int(input())

    if x > 2 and x % 2 == 0:
        print(x-2, 2)
    else:
        print(x-1, 1)
