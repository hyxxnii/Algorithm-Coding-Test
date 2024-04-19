import sys
input = sys.stdin.readline

# n, k = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# s, x, y = map(int, input().split())

# def virus(x, y):
#     global start_virus
    
#     check = False
#     for i in range(4):
#         nx = dx[i] + x
#         ny = dy[i] + y
#         if nx >= 0 and ny >= 0 and nx < n and ny < n:
#             if data[nx][ny] == 0:
#                 data[nx][ny] = start_virus
#                 check = True
#     return check

# def spread_virus():
#     global start_virus
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == start_virus:
#                 check = virus(i, j)
#                 if check: # 해당 바이러스 번호가 정상적으로 확산이 됐다면
#                     start_virus += 1
#             # 1초에 모든 바이러스 확산이 끝났다면 
#             if start_virus > k:
#                 start_virus = 1
#                 return 
            
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# start_virus = 1

# for _ in range(s):
#     spread_virus()

# print(data[x-1][y-1])

###############################
# BFS로 다시 풀기
############################### 
from collections import deque
n, k = map(int, input().split())
data = []
virus = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j], 0, i, j)) # 바이러스 번호순 정렬, 시간, 좌표
    
target_s, target_x, target_y = map(int, input().split())
virus.sort()
q = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행
while q:
    v, s, x, y = q.popleft()
    if s == target_s:
        break
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = v
                q.append((v, s+1, nx, ny))

print(data[target_x-1][target_y-1])