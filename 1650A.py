t = int(input())
for _ in range(t):
    s = input()
    c = input()

    if any(s[i] == c for i in range(0, len(s), 2)):
        print('YES')
    else:
        print('NO')
