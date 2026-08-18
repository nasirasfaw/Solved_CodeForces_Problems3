from math import ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))

turns = []
for i in range(len(a)):
    turns.append([i, ceil(a[i]/m)])
maxm = max(turns[i][1] for i in range(len(a)))

max_turns = []
for i in range(len(a)):
    if turns[i][1] == maxm:
        max_turns.append([i, turns[i][1]])

max_index = max(max_turns[i][0] for i in range(len(max_turns)))

print(max_index + 1)
