t = int(input())
for _ in range(t):
    m = [input() for _ in range(10)]

    count = 0
    for i in range(10):
        for j in  range(10):
            if m[i][j] == "X":
                count += min(i, j, 9-i, 9-j) + 1
    print(count)
