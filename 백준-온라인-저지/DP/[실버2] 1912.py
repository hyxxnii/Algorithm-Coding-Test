# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp[i]: 연속된 수 중 i가 마지막 숫자일 때의 가장 큰 합
dp = [-1001] * 100001
dp[1] = arr[0]

for i in range(1, n):
    dp[i+1] = max(arr[i], arr[i] + dp[i])

print(max(dp))
