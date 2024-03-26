# https://www.acmicpc.net/problem/2839
import sys
input = sys.stdin.readline
n = int(input())

dp = [-1] * 5001
dp[3] = 1
dp[5] = 1

if n <= 5:
    print(dp[n])

else:
    for i in range(6, n+1):
        kg_3 = dp[i-3]
        kg_5 = dp[i-5]
        
        if kg_3 > 0 and kg_5 > 0:
            dp[i] = min(kg_3+1, kg_5+1)
        elif kg_3 > 0 and kg_5 < 0:
            dp[i] = kg_3 + 1
        elif kg_3 < 0 and kg_5 > 0:
            dp[i] = kg_5 +1
        else:
            dp[i] = -1
    print(dp[n])