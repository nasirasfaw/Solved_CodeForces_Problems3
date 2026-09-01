n = int(input())
a = list(map(int, input().split()))
 
total = 0
i = 0
while total < n:
    total += a[i%7]
    if total >= n:
        print((i%7)+1)
        break
    else:
        i += 1
