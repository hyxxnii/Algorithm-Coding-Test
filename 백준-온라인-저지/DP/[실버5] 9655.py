# https://www.acmicpc.net/problem/9655

import sys
input = sys.stdin.readline

n = int(input())

# 1 또는 3개의 돌을 가져가고 남았을 때, 상근이의 승리 여부
dp = [0] * 1001
dp[1] = 1 # 돌이 1개 남았을 땐, 상근이가 이김 (1)

# 상근이가 돌을 가져갔을 때, 남아있는 돌의 수에 따른 다음 차례의 사람(창영)의 승패 여부
for i in range(2, n+1): # 현재 탁자 위 돌의 개수
    rock_1 = i - 1
    rock_3 = i - 3
    if dp[rock_1] + dp[rock_3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[n] == 1:
    print("SK")
else:
    print("CY")
    
###########################
# 근데 현재 탁자 위의 돌의 수가 홀수일 때 상근이가, 짝수일 때 창영이가 이기는 문제..!!!