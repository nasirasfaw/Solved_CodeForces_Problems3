from math import sqrt
t = int(input())
for _ in range(t):
    s = input()

    s1 = int(s)

    r = int(sqrt(s1))

    if r**2 == s1:
        print(r//2, r - r//2)
    else:
        print(-1)
