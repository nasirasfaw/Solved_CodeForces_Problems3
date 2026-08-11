n = int(input())
k = 1
height = 0
while n >= k*(k+1)//2:
    n = n - k*(k+1)//2
    k += 1
    height += 1

print(height)
