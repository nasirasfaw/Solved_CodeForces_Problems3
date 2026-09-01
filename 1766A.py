t = int(input())
for _ in range(t):
    n = int(input())

    n1 = [int(d) for d in str(n)]
    count = n1[0] + 9*(len(n1)-1)

    print(count)
