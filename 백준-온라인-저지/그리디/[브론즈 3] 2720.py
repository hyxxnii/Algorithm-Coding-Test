t = int(input())

coins = [25, 10, 5, 1]

for _ in range(t):
    res = []
    c = int(input())
    
    for coin in coins:
        res.append(c // coin)
        c = c % coin
    
    print(*res)