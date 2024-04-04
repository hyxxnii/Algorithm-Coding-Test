# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    if graph[x][y] == 1: # 이 조건문을 만났다는 것은 일단 단지가 있다는 뜻 => True 반환
        cnt += 1
        graph[x][y] = 0
        
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for i in result:
    print(i)