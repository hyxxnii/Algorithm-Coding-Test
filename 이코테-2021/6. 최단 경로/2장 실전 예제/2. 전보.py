import heapq
import sys
input = sys.stdin.readline

# 다익스트라 알고리즘
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
inf = 1e9
distance = [inf] * (n+1) # 최종 최단 거리가 저장될 리스트

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(c)

cnt = 0
max_dist = 0
for d in distance:
    if d != inf:
        cnt += 1
        max_dist = max(max_dist, d)

print(cnt-1, max_dist)