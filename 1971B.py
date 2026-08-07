t = int(input()) 
for _ in range(t):
    s = input()
    for i in range(1, len(s)):
        if len(s) > 1 and s[i-1] != s[i]:
            print("YES")
            s = s[i:] + s[:i]
            print(s)
            break
    else:
        print("NO")
