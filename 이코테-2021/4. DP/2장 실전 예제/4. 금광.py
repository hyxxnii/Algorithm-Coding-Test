import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    dp = []
    idx = 0
    for i in range(n):
        dp.append(tmp[idx:idx+m])
        idx += m
            
    for y in range(1, m): # 2번째 열부터
        for x in range(n): # x가 맨 위, 혹은 맨 아래인 경우도 생각
            if x == 0: # 왼쪽 위
                left_up = 0
            else:
                left_up = dp[x-1][y-1]
                
            if x == n-1: # 왼쪽 아래
                left_down = 0
            else:
                left_down = dp[x+1][y-1]
            
            left = dp[x][y-1]
            dp[x][y] = dp[x][y] + max(left_up, left_down, left)
            
    result =0
    for i in range(n):
        result = max(dp[i][m-1], result)
    print(result)
