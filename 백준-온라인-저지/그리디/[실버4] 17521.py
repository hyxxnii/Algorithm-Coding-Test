# https://www.acmicpc.net/problem/17521

import sys
input = sys.stdin.readline

n, w = map(int, input().split())
coins = list([int(input()) for _ in range(n)])

now = 0 # 현재 코인 보유량
c = coins[0]
for i in range(n-1):
    if now == 0 and c >= coins[i]:
        if coins[i] < coins[i+1]:
            c = coins[i]
            now += w // coins[i]
            w %= coins[i]
    elif now > 0 and c < coins[i]:
        if coins[i] > coins[i+1]:
            c = coins[i]
            w += now * coins[i]
            now = 0
            

if now > 0:
    w += now * coins[-1]
    
print(w)