# https://www.acmicpc.net/problem/1010
import sys
input = sys.stdin.readline

########################
# 1. 순열 공식 nCr = n! / (n-r)!r!
t = int(input())

def factorial(i):
    if i < 2:
        return 1
    return i * factorial(i-1)
    
for _ in range(t):
    n, m = map(int, input().split())
    result = factorial(m) / (factorial(m-n) * factorial(n))
    print(int(result))
    
######################## 
# 2. 다이나믹 동적프로그래밍
# 점화식: dp[n][m] = dp[n-1][m-1] + dp[n][m-1]
dp = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    for j in range(1, 31):
        if i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])