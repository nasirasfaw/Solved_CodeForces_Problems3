t = int(input())
for _ in range(t):
    s = input()
    m = int(s)

    a = [10**k for k in range(11)]

    for i in range(len(a)-1):
        if a[i] <= m and a[i+1] > m:
            print(m-a[i])
