# https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline

n = int(input())
drink = [int(input()) for _ in range(n)]

dp = [0] * (n+1)
dp[1] = drink[0]

if n == 1:
    print(max(dp))
else:
    dp[2] = drink[0] + drink[1]

    for i in range(2, n):
        dp[i+1] = max(drink[i] + drink[i-1] + dp[i-2],
                    drink[i] + dp[i-1],
                    dp[i])

    print(max(dp))