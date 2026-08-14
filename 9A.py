from math import gcd
y, w = map(int, input().split())

x = max(y, w)
a = (6-x+1) // gcd(6-x+1, 6) 
b = 6 // gcd(6-x+1, 6)

print(f"{a}/{b}")
