# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

parents = [0] * (n+1)
visited = [0] * (n+1)

def bfs(i):
    q = deque()
    q.append(i)
    while q:
        v = q.popleft()
        visited[v] = 1
        for child in graph[v]:
            if not visited[child]:
                parents[child] = v
                q.append(child)
    
    for i in parents[2:]:
        print(i, end='\n')

bfs(1)