# https://www.acmicpc.net/problem/4396
import sys
input = sys.stdin.readline

n = int(input())
data = [list(input().strip()) for _ in range(n)]
find = [list(input().strip()) for _ in range(n)]

result = [["."] * n for _ in range(n)]
# find는 이미 열린칸
# 열린 칸이 x일 때 => 1. data에서 해당 위치가 *이면 *로, .이면 find_bomb 함수
# 열린 칸이 .일 때 (닫힌 곳) => 그냥 .으로
def find_bomb(i, j):
    cnt = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x < 0 or y < 0 or x >= n or y >= n:
                continue
            if x == i and y == j:
                continue
            if data[x][y] == "*":
                cnt += 1
    return str(cnt)

def open_all_bomb():
    for i in range(n):
        for j in range(n):
            if data[i][j] == "*":
                result[i][j] = "*"
                
for i in range(n):
    for j in range(n):
        if find[i][j] == ".":
            if data[i][j] != "*":
                result[i][j] = "."
        
        else:
            if data[i][j] == "*": # 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 열리고 다른 모든 지점은 온점(.)
                open_all_bomb()
            else:
                result[i][j] = find_bomb(i, j)

for i in range(n):
    print(''.join(result[i]))