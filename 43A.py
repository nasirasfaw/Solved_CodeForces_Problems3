n = int(input())
s = [input() for _ in range(n)]

m = max(s.count(x) for x in s)

for x in s:
    if s.count(x) == m:
        print(x)
        break
