# https://www.acmicpc.net/problem/13549
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
inf = 1e9
# max_ = max(n, k)
graph = [[] for _ in range(100001)] # k+1번 노드까지 생성 가능 ("X-1"로 이동하는 경우 고려)
distance = [inf] * (100001)

def make_graph(node):
    # x+1
    if node + 1 <= 100000:
        graph[node].append((node+1, 1))
    # x-1
    if node - 1 > 0 and node - 1 <= 100000:
        graph[node].append((node-1, 1))
    
    # 2x
    if 2*node <= 100000:
        graph[node].append((2*node, 0))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        make_graph(now)
        # print("현재 노드: ", now)
        # print(graph[now])
        # print()
        for i in graph[now]: # i[0]:노드 번호, i[1]: 해당 노드까지 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

if n >= k:
    print(n-k)
else:
    dijkstra(n)
    print(distance[k])