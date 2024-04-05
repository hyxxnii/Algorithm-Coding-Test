a, b = map(int, input().split())

res = 1

while True:
    if b < a:
        res = -1
        break
    
    if b % 10 == 1:
        b = b // 10
    else:
        if b % 2 != 0:
            res = -1
            break
        b = b // 2 

    res += 1
    
    if b == a:
        break
    
print(res)