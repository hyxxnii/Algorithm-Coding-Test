## 문제 해석: 
# 0인 지점에서는 어쨌든 카운트가 됨
# 이때 0인 지점의 인접 노드를 모두 방문해서 방문 처리를 해주기 위해 DFS 함수로 재귀 함수를 수행

# 즉, 현재 노드가 0일 때, 그와 인접한 모든 노드들을 방문하면서 값이 0이라면 방문 처리(1)를 해줌으로써 아이스크림 개수 구하는 것
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

# DFS - 스택, 재귀
def dfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: # 아이스크램 개수 카운트가 되는데, 이때 인접 노드 0인 경우 방문 처리 해주기위해 상하좌우에 대해 재귀적 방문
        graph[x][y] = 1 # 방문 처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
        
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)