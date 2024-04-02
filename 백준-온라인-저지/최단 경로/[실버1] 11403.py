# https://www.acmicpc.net/problem/11403
import sys
input = sys.stdin.readline

# 플로이드-워셜
n = int(input())
inf = 1e9
graph = [[inf] * n for _ in range(n)]
for i in range(n):
    info = list(map(int, input().split()))
    for j in range(len(info)):
        if info[j] == 1:
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] < inf:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()