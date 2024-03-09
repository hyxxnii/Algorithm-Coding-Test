n, m = map(int, input().split())
s = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    
    if a == 1: 
        s[b-1] = c
        
    elif a == 2:
        tmp = list(map(lambda x: (x+1)%2, s[b-1:c]))
        s[b-1:c] = tmp
    
    else:
        tmp = [(a+1)%2] * (c-b+1)
        s[b-1:c] = tmp
    
print(*s)