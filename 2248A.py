t = int(input())
for _ in range(t):
    s = input()
    
    i = s.index("0")
    j = s.index("1")
    k1, k2 = min(i, j), max(i, j)

    s = s[:k1] + s[k1+1:k2] + s[k2+1:]

    print(s)
