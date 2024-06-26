# https://www.acmicpc.net/problem/1463

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (10**6 + 1)

dp[1], dp[2], dp[3] = 0, 1, 1

for i in range(4, n+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    
print(dp[n])