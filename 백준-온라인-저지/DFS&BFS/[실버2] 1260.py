# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

graph = [sorted(graph[i]) for i in range(len(graph))]
# 정렬을 따로 안해주려면, n+1 x n+1 의 행렬 초기화로 진행
# graph = [[0]*(n+1) for _ in range(n+1)]
# graph[i][j] =1 

dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

# DFS
def dfs(i):
    if not dfs_visited[i]:
        dfs_visited[i] = 1
        print(i, end=' ')
        for j in graph[i]:
            dfs(j)

def bfs(i):
    q = deque()
    q.append(i)
    bfs_visited[i] = 1
    while q:
        pop = q.popleft()
        print(pop, end=' ')
        for j in graph[pop]:
            if not bfs_visited[j]:
                q.append(j)
                bfs_visited[j] = 1
                
dfs(v)
print()
bfs(v)