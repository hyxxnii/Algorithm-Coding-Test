import sys
input = sys.stdin.readline

# 플로이드 워셜 알고리즘
n, m = map(int, input().split())
inf = 1e9
graph = [[inf] * (n+1) for _ in range(n+1)]

# 자기 자신 = 0
for i in range(1, n+1):
    graph[i][i] = 0
    
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

result = graph[1][k] + graph[k][x]
if result >= inf:
    print("-1")
else:
    print(result)