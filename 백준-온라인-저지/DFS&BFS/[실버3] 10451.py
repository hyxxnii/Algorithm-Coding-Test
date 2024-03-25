# https://www.acmicpc.net/problem/10451
import sys

test = int(sys.stdin.readline())

def dfs(i):
    if not visited[graph[i]-1]:
        visited[graph[i]-1] = 1
        dfs(graph[i]-1)

for _ in range(test):
    result = 0
    n = int(sys.stdin.readline())

    # 다른 버전
    graph = list(map(int, sys.stdin.readline().split()))
    visited = [0] * n
    for i, g in enumerate(graph):
        if not visited[i]:
            visited[i] = 1
            dfs(i)
            result += 1
    print(result)