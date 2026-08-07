n, m = map(int, input().split())

min_ab = {}
for _ in range(m):
    a, b = input().split()

    if len(a) <= len(b):
        min_ab[a] = a
    else:
        min_ab[a] = b

c = input().split()

for x in c:
    print(min_ab[x], end=" ")
