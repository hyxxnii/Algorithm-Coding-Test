from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [-1] * (n+1)
dist[x] = 0 # 출발지점 거리=0


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
def bfs(x):
    q = deque()
    q.append(x)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if dist[i] == -1:
                dist[i] = dist[node] + 1
                q.append(i)

bfs(x)
check = False
for i in range(n+1):
    if dist[i] == k:
        print(i)
        check = True
if not check:
    print("-1")
