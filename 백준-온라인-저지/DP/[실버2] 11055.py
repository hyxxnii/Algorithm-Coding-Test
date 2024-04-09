# https://www.acmicpc.net/problem/11055

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 1000 # dp[i]: i번째 숫자가 마지막으로 오는 부분 수열 중 가장 큰 값
dp[0] = arr[0]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j]) #max(dp[i], arr[i] + dp[j])
    if dp[i] == 0:
        dp[i] = arr[i]
    
# print(dp[:10])
print(max(dp))