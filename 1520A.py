t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    s1 = []
    i = 0
    for j in range(1, n):
        if s[j] != s[j-1]:
            s1.append(set(s[i:j]))
            i = j
    s1.append(set(s[i:]))

    if all(s1.count(x) == 1 for x in s1):
        print("YES")
    else:
        print("NO")
