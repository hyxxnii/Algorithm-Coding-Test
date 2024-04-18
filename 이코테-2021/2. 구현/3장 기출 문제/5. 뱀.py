import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

l = int(input())
info = []
for _ in range(l):
    i = input().split()
    x, c = int(i[0]), i[1] # c: L(왼쪽), D(오른쪽) 으로 90도 방향 회전
    info.append((x, c))

# 현재 동쪽 -> 90도 회전씩 차례대로 동남서북 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate(direction, c):
    # direction: 현재 방향
    # c: 회전 방향
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
    
def simulate():
    x, y = 0, 0 # 현재 뱀 머리 위치
    board[x][y] = 2 # 뱀이 있는 위치 = 2
    sec = 0 # 시간
    d = 0 # 방향(현재 동쪽)
    info_idx = 0 # 방향 회전 정보
    tail = [(x, y)] # 뱀이 차지하고 있는 칸 기록 (꼬리가 맨 왼쪽)
    while True:
        sec += 1
        nx = dx[d] + x
        ny = dy[d] + y
        
        # 뱀 머리가 벽 또는 뱀의 몸에 부딪히지 않았다면
        if nx >= 0 and ny >= 0 and nx < n and ny < n and board[nx][ny] != 2:
            # 이동 및 꼬리 기록
            if board[nx][ny] == 1: # 사과가 있다면
                board[nx][ny] = 2 # 사과 먹고 뱀이 차지
                tail.append((nx, ny))
            else: # 사과가 없다면
                board[nx][ny] = 2 # 일단 이동하고
                tail.append((nx, ny)) # 꼬리 기록
                tail_x, tail_y = tail.pop(0) # 꼬리 제거
                board[tail_x][tail_y] = 0
        else:
            return sec

        x, y = nx, ny
        if info_idx < l and sec == info[info_idx][0]:
            d = rotate(d, info[info_idx][1])
            info_idx += 1
            
print(simulate())