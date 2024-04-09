# https://www.acmicpc.net/problem/1890

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 1. BFS => 메모리 초과
# from collections import deque

# def bfs(x, y):
#     q.append((x, y))
#     result = 0
    
#     while q:
#         x, y = q.popleft()
#         dx = [board[x][y], 0] # 아래
#         dy = [0, board[x][y]] # 오른쪽
        
#         for i in range(2):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx == N-1 and ny == N-1:
#                 result += 1
#                 break
#             if nx >= 0 and ny >= 0 and nx < N and ny < N:
#                 q.append((nx, ny))
    
#     return result

# q = deque()
# print(bfs(0, 0))

# DP
dp = [[0] * N for _ in range(N)] # 현재 칸에 도달할 수 있는 경우의 수의 누적
dp[0][0] = 1

for i in range(N): # 행
    for j in range(N): # 열
        if i == N-1 and j == N-1:
            break
        # 오른쪽 이동
        nj = j + board[i][j]
        if nj < N:
            dp[i][nj] += dp[i][j]
        
        # 아래 이동
        ni = i + board[i][j]
        if ni < N:
            dp[ni][j] += dp[i][j]

print(dp[N-1][N-1])