n, a, b = map(int, input().split())

count = 0
for i in range(n):
    if i <= b and n-i > a:
        count += 1

print(count)
