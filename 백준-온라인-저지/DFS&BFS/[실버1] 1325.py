# https://www.acmicpc.net/problem/1325
## 시간 초과 해결 못함.. DFS/BFS 모두 안돼.. python 거지같아...

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[j].append(i)

def bfs(start):
    cnt = 0
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    
    while q:
        node = q.popleft()
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                cnt += 1
    return cnt

result = []
for i in range(1, n+1): # 1번부터 차례대로 해킹되는 컴퓨터 수 구하기
    result.append(bfs(i))

max_ = max(result)
for i in range(n):
    if result[i] == max_:
        print(i+1, end=' ')