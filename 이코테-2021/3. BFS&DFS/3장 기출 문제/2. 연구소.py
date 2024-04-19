import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            # 바이러스/벽이 아닌 곳에 확산
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)

def get_safe_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1
    return score

def dfs(cnt):
    global result
    
    if cnt == 3: # 벽 개수
        for i in range(n):
            for j in range(m):
                # 3개의 벽 설치 장소가 매번 다르므로 임시 행렬에서 dfs 진행
                tmp[i][j] = graph[i][j]
        # 바이러스 위치에서 퍼뜨리기
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_safe_score())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 0인 곳 무작위에 벽 3개 설치
                graph[i][j] = 1
                cnt += 1
                dfs(cnt) # 벽 세우고 다시 dfs 함수 재귀 수행
                # 벽 3개 설치 및 점수 계산 후 다른 곳에 벽 세우기 위해 원상복구
                graph[i][j] = 0
                cnt -= 1
result = 0
dfs(0)
print(result)