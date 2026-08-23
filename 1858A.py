t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    if a > b or (a == b and c % 2 != 0):
        print("First")
    else:
        print("Second")
