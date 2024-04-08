# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 11

for i in range(11):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])