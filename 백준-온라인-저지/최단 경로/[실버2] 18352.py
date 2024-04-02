# https://www.acmicpc.net/problem/18352

import heapq
import sys
input = sys.stdin.readline

# 다익스트라 알고리즘

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
inf = 1e9
distance = [inf] * (n+1)

for _ in range(m): 
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]: # i[0]: 인접노드, i[1]: 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)
result = []
for i, dist in enumerate(distance):
    if dist == k:
        result.append(i)

if len(result) == 0:
    print("-1")
else:
    for i in result:
        print(i)