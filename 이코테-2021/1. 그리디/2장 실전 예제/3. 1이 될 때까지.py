n, k = map(int, input().split())

cnt = 0

while True:
    while n % k == 0:
        n = n // k
        cnt += 1
        
    if n == 1:
        break
    
    n -= 1
    cnt += 1
    if n == 1:
        break
    
print(cnt)