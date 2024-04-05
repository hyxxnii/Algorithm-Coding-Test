# https://www.acmicpc.net/problem/16918

from collections import deque
import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

def bfs(q, graph):
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < r and ny < c:
                graph[nx][ny] = '.'

def solve(t):
    global graph, q
    if t == 1:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append((i, j))
    
    elif t % 2 == 0:
        graph = [['O']*c for _ in range(r)]
    
    else:
        bfs(q, graph)
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append((i, j))
    
for t in range(1, n+1):
    solve(t)
    
for bomb in graph:
    print(''.join(bomb))