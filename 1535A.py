t = int(input())
for _ in range(t):

    s1, s2, s3, s4 = map(int, input().split())

    s = [s1, s2, s3, s4]

    maxm = [max(s1, s2), max(s3, s4)]

    sr = sorted(s)
    if set(maxm) == set([sr[2], sr[3]]):
        print("YES")
    else:
        print("NO")
