a, b = map(int, input().split())

c = min(a, b)  #gcd(a!, b!) = c!

c_factorial = 1

for i in range(1, c+1):
    c_factorial *= i

print(c_factorial)
