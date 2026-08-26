t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    a = []
    for i in range(n):
        s1 = list(s)

        if s1[i] == '0':
            s1[i] = '1'
        else:
            s1[i] = '0'
        a.append(''.join(s1))

    s2 = ''.join(a)

    print(s2.count('1'))
