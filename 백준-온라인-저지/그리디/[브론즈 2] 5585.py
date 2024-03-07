m = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

res = 0
for c in coins:
    res +=  m // c
    m = m % c

print(res)