import string
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    letts = list(string.ascii_lowercase)
    digits = list("0123456789")
    digletts = digits + letts

    for i in range(n):
        if any(digletts.index(s[i]) > digletts.index(s[j]) for j in range(i+1, n)):
            print("NO")
            break
    else:
        print("YES")
