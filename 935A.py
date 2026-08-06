n = int(input())

count = 0
for k in range(1, n//2+1):
    if (n-k) % k == 0:
        count += 1

print(count)
