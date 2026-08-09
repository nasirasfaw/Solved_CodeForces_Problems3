from bisect import bisect_right
n = int(input())
x = list(map(int, input().split()))
q = int(input())

x.sort()
m = []
for i in range(q):
    m.append(int(input()))

for i in range(q):
    print(bisect_right(x, m[i]))
