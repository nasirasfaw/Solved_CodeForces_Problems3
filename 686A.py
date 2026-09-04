n, x = map(int, input().split())
a = []
for _ in range(n):
    ch, d = input().split()
    d = int(d)
    a.append([ch, d])
distressed = 0
i = 1
while i < n:
    if a[i-1][0] == "+":
        x += a[i-1][1]
    else:
        if x >= a[i-1][1]:
            x -= a[i-1][1]
        else:
            distressed += 1
    i += 1
if a[n-1][0] == "+":
    x += a[n-1][1]
else:
    if x < a[n-1][1]:
        distressed += 1
    else:
        x -= a[n-1][1]
print(x, distressed)
