# https://www.acmicpc.net/problem/2606
import sys

## 1차 풀이
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1

com = [0] * n
# DFS
def dfs(i):
    com[i] = 1 # 감염 o
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            if com[j] == 0:
                dfs(j)

dfs(0)
print(sum(com[1:]))


## 2차 풀이
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n)] # 바로 빈 리스트 초기화도 됨

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)
    
visited = [0] * n
def dfs(i):
    visited[i] = 1 # 감염 o
    for child in graph[i]:
        if visited[child] == 0:
            dfs(child)
    
dfs(0)
print(sum(visited) - 1)