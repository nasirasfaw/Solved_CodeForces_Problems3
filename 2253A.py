lm = 2*10**5 + 1
prime = [True]*(lm + 1)
prime[0] = prime[1] = False
i = 2
while i*i < lm+1:
    if prime[i]:
        j = i * i
        while j < lm+1:
            prime[j] = False
            j += i
    i += 1
    
t = int(input())

for _ in range(t):
    n = int(input())
  
    print("YES" if prime[n+1] else "NO")
