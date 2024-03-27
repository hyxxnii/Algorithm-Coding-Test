import sys

input = sys.stdin.readline
n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

dp = [10001] * (m+1) # 화폐 1원부터
dp[0] = 0

for i in range(n): # [2, 3]
    for j in range(money[i], m+1):
        dp[j] = min(dp[j-money[i]] + 1, dp[j])

if dp[m] == 10001:
    print("-1")
else:
    print(dp[m])