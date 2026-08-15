t = int(input())
for _ in range(t):
    n = int(input())
    mat = [input() for _ in range(n)]

    notes = []

    for i in range(n):
        notes.append(mat[n-1-i].index("#")+1)
        
    print(*notes)
